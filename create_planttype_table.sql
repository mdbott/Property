-- Table: botanical_name

-- DROP TABLE planttype;
CREATE SEQUENCE planttype_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;
ALTER TABLE planttype_id_seq
  OWNER TO postgres;
CREATE TABLE planttype
(
  id smallint NOT NULL DEFAULT nextval('planttype_id_seq'::regclass),
  type character varying(100) DEFAULT NULL::character varying,
  CONSTRAINT planttype_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE planttype
  OWNER TO postgres;

