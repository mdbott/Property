-- View: vegetation_view

-- DROP VIEW vegetation_view;

CREATE OR REPLACE VIEW vegetation_view AS 
 SELECT vegetation_view.row_number,
    vegetation_view.vegetationid,
    vegetation_view.botanicalid,
    vegetation_view.legacy_pfaf_latin_name,
    vegetation_view.family,
    vegetation_view.genus,
    vegetation_view.species,
    vegetation_view.ssp,
    vegetation_view.common_name,
    vegetation_view.type,
    vegetation_view.locations,
    vegetation_view.dripline_radius,
    vegetation_view.comment,
    vegetation_view.germination_date
   FROM ( SELECT row_number() OVER (ORDER BY vegetation.id) AS row_number,
            vegetation.id AS vegetationid,
            botanical_name.id AS botanicalid,
            botanical_name.legacy_pfaf_latin_name,
            botanical_name.family,
            botanical_name.genus,
            botanical_name.species,
            botanical_name.ssp,
            botanical_name.common_name,
            botanical_name.type,
            vegetation.locations,
            culture.width_centimeters AS dripline_radius,
            vegetation.comment,
            vegetation.germination_date
           FROM vegetation
             LEFT JOIN botanical_name ON vegetation.botanical_name_id = botanical_name.id
             LEFT JOIN culture ON vegetation.botanical_name_id = culture.id) vegetation_view;

ALTER TABLE vegetation_view
  OWNER TO postgres;
COMMENT ON VIEW vegetation_view
  IS '-- View: vegetation_view';

-- Rule: view_delete ON vegetation_view

-- DROP RULE view_delete ON vegetation_view;

CREATE OR REPLACE RULE view_delete AS
    ON DELETE TO vegetation_view DO INSTEAD  DELETE FROM vegetation
  WHERE vegetation.id = old.vegetationid;

-- Rule: view_insert ON vegetation_view

-- DROP RULE view_insert ON vegetation_view;

CREATE OR REPLACE RULE view_insert AS
    ON INSERT TO vegetation_view DO INSTEAD  INSERT INTO vegetation (botanical_name_id, locations, comment, germination_date)
  VALUES (new.botanicalid, new.locations, new.comment, new.germination_date);

-- Rule: view_update ON vegetation_view

-- DROP RULE view_update ON vegetation_view; 
CREATE OR REPLACE RULE view_update AS
    ON UPDATE TO vegetation_view DO INSTEAD ( UPDATE vegetation SET botanical_name_id = new.botanicalid, locations = new.locations, comment = new.comment, germination_date = new.germination_date
  WHERE vegetation.id = new.vegetationid;
 UPDATE botanical_name SET type = new.type
  WHERE botanical_name.id = new.botanicalid;
);