-- Pattern search
CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(user_id INT, username TEXT, surname TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT *
    FROM phonebook
    WHERE username ILIKE '%' || pattern || '%'
       OR surname ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- Pagination
CREATE OR REPLACE FUNCTION get_phonebook_page(limit_val INT, offset_val INT)
RETURNS TABLE(user_id INT, username TEXT, surname TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT *
    FROM phonebook
    ORDER BY user_id
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;