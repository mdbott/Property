
-- Create the view

CREATE OR REPLACE VIEW emp_entity AS SELECT employee_name, entity_name, address
 FROM entities JOIN employees USING (entity_name);

-- Create the Trigger

CREATE OR REPLACE FUNCTION dml_emp_entity () RETURNS trigger LANGUAGE plpgsql AS $$
 DECLARE
   vrecord RECORD;
 BEGIN
   IF TG_OP = 'INSERT' THEN
     -- Does the record exist in entity ?
     SELECT entity_name,address INTO vrecord FROM entities WHERE entity_name=NEW.entity_name;
     IF NOT FOUND THEN
       INSERT INTO entities (entity_name,address) VALUES (NEW.entity_name, NEW.address);
     ELSE
       IF vrecord.address != NEW.address THEN
       RAISE EXCEPTION 'There already is a record for % in entities. Its address is %. It conflics with your address %',
                       NEW.entity_name, vrecord.address, NEW.address USING ERRCODE = 'unique_violation';
       END IF;
     END IF; -- Nothing more to do, the entity already exists and is OK
     -- We now try to insert the employee data. Let's directly try an INSERT
     BEGIN
       INSERT INTO employees (employee_name, entity_name) VALUES (NEW.employee_name, NEW.entity_name);
       EXCEPTION WHEN unique_violation THEN
         RAISE EXCEPTION 'There is already an employee with this name %', NEW.employee_name USING ERRCODE = 'unique_violation';
     END;
   RETURN NEW; -- The trigger succeeded
   END IF;
 END
 $$
 ;

-- Apply the trigger to the view

CREATE TRIGGER trig_dml_emp_entity INSTEAD OF INSERT OR UPDATE OR DELETE ON emp_entity FOR EACH ROW EXECUTE PROCEDURE dml_emp_entity ();
