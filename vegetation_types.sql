-- View: vegetation_types
--
-- DROP VIEW vegetation_types;

CREATE OR REPLACE VIEW vegetation_types AS 
SELECT 
  vegetation_types.row_number,
  vegetation_types.botanicalid,
  vegetation_types.family,
  vegetation_types.genus,
  vegetation_types.species,
  vegetation_types.common_name,
  vegetation_types.typeid,
  vegetation_types.type
FROM  ( SELECT row_number() OVER (ORDER BY botanical_name.common_name) AS row_number,
            botanical_name.id AS botanicalid,
            botanical_name.legacy_pfaf_latin_name,
            botanical_name.family,
            botanical_name.genus,
            botanical_name.species,
            botanical_name.common_name,
            botanical_name.type AS typeid,
            planttype.type
           FROM botanical_name
             LEFT JOIN planttype ON botanical_name.type = planttype.id
           WHERE botanical_name.id IN
            (SELECT DISTINCT botanical_name_id FROM vegetation)) vegetation_types;
ALTER TABLE vegetation_types
  OWNER TO postgres;
COMMENT ON VIEW vegetation_types
  IS '-- View: vegetation_types';

  -- Rule: view_update ON vegetation_view

-- DROP RULE view_update ON vegetation_view;

CREATE OR REPLACE RULE view_type_update AS
    ON UPDATE TO vegetation_types DO INSTEAD  UPDATE botanical_name SET type = new.typeid
  WHERE botanical_name.id = new.botanicalid;
