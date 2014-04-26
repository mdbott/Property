CREATE OR REPLACE VIEW vegetation_view AS
SELECT 
  vegetation.botanical_name_id,
  botanical_name.legacy_pfaf_latin_name, 
  botanical_name.family, 
  botanical_name.genus, 
  botanical_name.species, 
  botanical_name.ssp, 
  botanical_name.common_name, 
  vegetation.locations
FROM public.vegetation
LEFT JOIN public.botanical_name ON vegetation.botanical_name_id = botanical_name.id;

