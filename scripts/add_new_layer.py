#!/usr/bin/python

__author__ = 'max'

import psycopg2
import argparse


def create_table(connection, table_name, table_schema):
    try:
        cur = connection.cursor()
        cur.execute("DROP TABLE IF EXISTS %s" % table_name)
        cur.execute("CREATE TABLE %s %s;" % (table_name, table_schema))
        connection.commit()
    except psycopg2.DatabaseError, e:
        if connection:
            connection.rollback()
        print 'Error %s' % e


def add_geom_col(connection, table, column, gtype, srid=3857, dim=2):
    """!Add a geometry column to the table.
    @connection             : Database connection.
    @param table            : Name of the table.
    @param column           : Name of the column for adding.
    @param gtype            : Geometry type of the new column.
    @param srid             : Spatial reference for the column.
    @param dim              : Dimension of the geometry. default is 2.
    """
    # Make a SQL statement.
    parse = "'public','" + table + "','" + column + "'," + str(srid) + ",'" + gtype + "'," + str(dim)
    try:
        cur = connection.cursor()
        sql_addgeomcol = 'SELECT AddGeometryColumn (' + parse + ');'
        # Execute the SQL statement.
        cur.execute(sql_addgeomcol)
        connection.commit()
    except psycopg2.DatabaseError, e:
        if connection:
            connection.rollback()
        print 'Error %s' % e


def create_insert_rule(connection, table_name, view_name):
    """!Add an insert rule to the database.
    @param table_name       : Name of the underlying table to be updated.
    @param view_name        : Name of the view being updated.
    """
    try:
        cur = connection.cursor()
        rule_name = view_name + "_insert"
        insert_rule_template = """
        CREATE OR REPLACE RULE {rulename} AS
        ON INSERT TO {viewname} DO INSTEAD
        INSERT INTO {tablename}
        (botanical_name_id, locations, comment)
        VALUES (new.botanicalid, new.locations, new.comment);
        """
        rule_sql = insert_rule_template.format(rulename=rule_name, viewname=view_name, tablename=table_name)

        # Execute the SQL statement.
        cur.execute(rule_sql)
        connection.commit()
    except psycopg2.DatabaseError, e:
        if connection:
            connection.rollback()
        print 'Error %s' % e


def create_update_rule(connection, table_name, view_name):
    """!Add an update rule to the database.
    @param table_name       : Name of the underlying table to be updated.
    @param view_name        : Name of the view being updated.
    """
    try:
        cur = connection.cursor()
        rule_name = view_name + "_update"
        update_rule_template = """
        CREATE OR REPLACE RULE {rulename} AS
        ON UPDATE TO {viewname} DO INSTEAD
        UPDATE {tablename}
        SET botanical_name_id = new.botanicalid,
        locations = new.locations,
        comment = new.comment
        WHERE {tablename}.id = new.vegetationid;
        """
        rule_sql = update_rule_template.format(rulename=rule_name, viewname=view_name, tablename=table_name)

        # Execute the SQL statement.
        cur.execute(rule_sql)
        connection.commit()
    except psycopg2.DatabaseError, e:
        if connection:
            connection.rollback()
        print 'Error %s' % e


def create_delete_rule(connection, table_name, view_name):
    """!Add a delete rule to the database.
    @param table_name       : Name of the underlying table to be updated.
    @param view_name        : Name of the view being updated.
    """
    try:
        cur = connection.cursor()
        rule_name = view_name + "_delete"
        delete_rule_template = """
        CREATE OR REPLACE RULE {rulename} AS
        ON DELETE TO {viewname} DO INSTEAD
        DELETE FROM {tablename}
        WHERE {tablename}.id = old.vegetationid;
        """
        rule_sql = delete_rule_template.format(rulename=rule_name, viewname=view_name, tablename=table_name)

        # Execute the SQL statement.
        cur.execute(rule_sql)
        connection.commit()
    except psycopg2.DatabaseError, e:
        if connection:
            connection.rollback()
        print 'Error %s' % e


def create_view(connection, view_name, view_query):
    """
    Create a named view on a connection.

    Returns True if a new view was created (or an existing one updated), or
    False if nothing was done.

    If ``update`` is True (default), attempt to update an existing view. If the
    existing view's schema is incompatible with the new definition, ``force``
    (default: False) controls whether or not to drop the old view and create
    the new one.
    """

    try:
        cur = connection.cursor()
        cur.execute('CREATE OR REPLACE VIEW {0} AS {1};'.format(view_name, view_query))
    except psycopg2.DatabaseError, e:
        if connection:
            connection.rollback()
        print 'Error %s' % e


def main():
    # parse command line options
    parser = argparse.ArgumentParser(description="Add a new plant layer (table & view) to the database")
    parser.add_argument('name', help="name of the plant layer to add")
    args = parser.parse_args()
    table_name = args.name
    # Connect to the database
    conn = psycopg2.connect("host='192.168.10.100' dbname='eden' user='postgres' password='mega^0lt'")

    # Setup the table
    table_schema = """
    (id SERIAL PRIMARY KEY,
     botanical_name_id smallint NOT NULL DEFAULT (1)::SMALLINT,
     comment TEXT
     )"""
    create_table(conn, table_name, table_schema)
    add_geom_col(conn, table_name, 'locations', 'Point')

    # Setup the view
    view_name = table_name + "_view"
    query_template = """
    SELECT {viewname}.row_number,
    {viewname}.vegetationid,
    {viewname}.botanicalid,
    {viewname}.legacy_pfaf_latin_name,
    {viewname}.family,
    {viewname}.genus,
    {viewname}.species,
    {viewname}.ssp,
    {viewname}.common_name,
    {viewname}.locations,
    {viewname}.hardyness,
    {viewname}.range,
    {viewname}.habitat,
    {viewname}.habit,
    {viewname}.persistance,
    {viewname}.height,
    {viewname}.width,
    {viewname}.nitrogen_fixer,
    {viewname}.cultivation_details,
    {viewname}.propagation_details,
    {viewname}.known_hazards,
    {viewname}.comment
    FROM ( SELECT row_number() OVER (ORDER BY {tablename}.id) AS row_number,
            {tablename}.id AS vegetationid,
            botanical_name.id AS botanicalid,
            botanical_name.legacy_pfaf_latin_name,
            botanical_name.family,
            botanical_name.genus,
            botanical_name.species,
            botanical_name.ssp,
            botanical_name.common_name,
            {tablename}.locations,
            culture.hardyness,
            culture.range,
            culture.habitat,
            culture.habit,
            culture.deciduous_evergreen AS persistance,
            culture.height_centimeters AS height,
            culture.width_centimeters AS width,
            culture.nitrogen_fixer,
            cultural_notes.cultivation_details,
            cultural_notes.propagation_details,
            cultural_notes.known_hazards,
            {tablename}.comment
           FROM {tablename}
             LEFT JOIN botanical_name ON {tablename}.botanical_name_id = botanical_name.id
             LEFT JOIN culture ON {tablename}.botanical_name_id = culture.id
             LEFT JOIN cultural_notes ON {tablename}.botanical_name_id = cultural_notes.id
             ) {viewname};
    """
    query = query_template.format(viewname=view_name, tablename=table_name)
    create_view(conn, view_name, query)
    # Finally create the insert, update & delete rules for the view
    create_insert_rule(conn, table_name, view_name)
    create_update_rule(conn, table_name, view_name)
    create_delete_rule(conn, table_name, view_name)
    # Finally close the connection to the database
    if conn:
            conn.close()

if __name__ == "__main__":
    main()