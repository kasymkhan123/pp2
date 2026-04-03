-- Upsert (insert or update)
CREATE OR REPLACE PROCEDURE upsert_user(p_username TEXT, p_surname TEXT, p_phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_username) THEN
        UPDATE phonebook
        SET phone = p_phone, surname = p_surname
        WHERE username = p_username;
    ELSE
        INSERT INTO phonebook(username, surname, phone)
        VALUES (p_username, p_surname, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;


-- Bulk insert with validation
CREATE OR REPLACE PROCEDURE insert_many_users(
    names TEXT[],
    surnames TEXT[],
    phones TEXT[]
)
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1)
    LOOP
        IF phones[i] ~ '^\+?[0-9]{5,15}$' THEN
            CALL upsert_user(names[i], surnames[i], phones[i]);
        ELSE
            RAISE NOTICE 'Invalid phone: %', phones[i];
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;


-- Delete
CREATE OR REPLACE PROCEDURE delete_user(p_value TEXT)
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = p_value
       OR phone = p_value;
END;
$$ LANGUAGE plpgsql;