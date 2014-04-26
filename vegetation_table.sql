
-- Sequence: botanical_name_id_seq

-- DROP SEQUENCE botanical_name_id_seq;

CREATE SEQUENCE vegetation_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;
ALTER TABLE vegetation_id_seq
  OWNER TO postgres;




-- Table: vegetataion

-- DROP TABLE vegetation;

CREATE TABLE vegetation
(
  id smallint NOT NULL DEFAULT nextval('vegetation_id_seq'::regclass),
  botanical_name_id smallint NOT NULL DEFAULT 1::smallint,
  locations geometry(Point,3857),
  CONSTRAINT vegetation_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE vegetation
  OWNER TO postgres;

