-- Sequence: polyculture_notes_id_seq

-- DROP SEQUENCE polyculture_notes_id_seq;

CREATE SEQUENCE polyculture_notes_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 7414
  CACHE 1;
ALTER TABLE polyculture_notes_id_seq
  OWNER TO postgres;

-- Table: polyculture_notes

-- DROP TABLE polyculture_notes;

CREATE TABLE polyculture_notes
(
  id smallint NOT NULL DEFAULT nextval('polyculture_notes_id_seq'::regclass),
  locations geometry(Point,3857),
  notes text,
)
WITH (
  OIDS=FALSE
);
ALTER TABLE polyculture_notes
  OWNER TO postgres;
