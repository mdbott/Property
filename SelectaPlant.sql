SELECT 
  botanical_name.common_name, 
  botanical_name.id
FROM 
  public.botanical_name
WHERE 
  botanical_name.common_name LIKE '%oak%';
