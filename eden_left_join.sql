SELECT * FROM public.vegetation
LEFT JOIN public.botanical_name ON vegetation.botanical_name_id = botanical_name.id
LEFT JOIN public.comments ON vegetation.botanical_name_id =  comments.parent_id;
