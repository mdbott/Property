CREATE OR REPLACE VIEW species_count_view AS 
SELECT 
species_count.row_number,
botanical_name.common_name,
species_count.num,
botanical_name.type as typeid,
planttype.type,
botanical_name.genus,
botanical_name.species
FROM (SELECT
  row_number() OVER (ORDER BY botanical_name_id) AS row_number,
  botanical_name_id,
  COUNT(*) AS num
FROM vegetation
   GROUP BY vegetation.botanical_name_id) species_count
LEFT JOIN botanical_name ON species_count.botanical_name_id = botanical_name.id
LEFT JOIN planttype ON botanical_name.type = planttype.id
ORDER BY row_number;
 