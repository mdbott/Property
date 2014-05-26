-- View: eucaluptus_view

-- DROP VIEW eucaluptus_view;

CREATE OR REPLACE VIEW eucaluptus_view AS 
 SELECT eucaluptus_view.row_number,
    eucaluptus_view.vegetationid,
    eucaluptus_view.botanicalid,
    eucaluptus_view.legacy_pfaf_latin_name,
    eucaluptus_view.family,
    eucaluptus_view.genus,
    eucaluptus_view.species,
    eucaluptus_view.ssp,
    eucaluptus_view.common_name,
    eucaluptus_view.locations,
    eucaluptus_view.dripline_radius,
    eucaluptus_view.comment
   FROM ( SELECT row_number() OVER (ORDER BY vegetation.id) AS row_number,
            vegetation.id AS vegetationid,
            botanical_name.id AS botanicalid,
            botanical_name.legacy_pfaf_latin_name,
            botanical_name.family,
            botanical_name.genus,
            botanical_name.species,
            botanical_name.ssp,
            botanical_name.common_name,
            vegetation.locations,
            vegetation.dripline_radius,
            vegetation.comment
           FROM vegetation
      LEFT JOIN botanical_name ON vegetation.botanical_name_id = botanical_name.id) eucaluptus_view
   WHERE eucaluptus_view.genus LIKE '%Eucalyptus%';

ALTER TABLE eucaluptus_view
  OWNER TO postgres;
COMMENT ON VIEW eucaluptus_view
  IS '-- View: eucaluptus_view';

-- Rule: view_delete ON eucaluptus_view

-- DROP RULE view_delete ON eucaluptus_view;

CREATE OR REPLACE RULE view_delete AS
    ON DELETE TO eucaluptus_view DO INSTEAD  DELETE FROM vegetation
  WHERE vegetation.id = old.vegetationid;

-- Rule: view_insert ON eucaluptus_view

-- DROP RULE view_insert ON eucaluptus_view;

CREATE OR REPLACE RULE view_insert AS
    ON INSERT TO eucaluptus_view DO INSTEAD  INSERT INTO vegetation (botanical_name_id, locations, dripline_radius, comment)
  VALUES (new.botanicalid, new.locations, new.dripline_radius, new.comment);

-- Rule: view_update ON eucaluptus_view

-- DROP RULE view_update ON eucaluptus_view;

CREATE OR REPLACE RULE view_update AS
    ON UPDATE TO eucaluptus_view DO INSTEAD  UPDATE vegetation SET botanical_name_id = new.botanicalid, locations = new.locations, dripline_radius = new.dripline_radius, comment = new.comment
  WHERE vegetation.id = new.vegetationid;
