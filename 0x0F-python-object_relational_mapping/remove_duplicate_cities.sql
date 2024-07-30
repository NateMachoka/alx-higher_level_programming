#!/usr/bin/node

USE hbtn_0e_4_usa
CREATE TEMPORARY TABLE temp_duplicates AS
SELECT MIN(id) AS min_id
FROM cities
GROUP BY state_id, name;

DELETE FROM cities
WHERE id NOT IN (
    SELECT min_id
    FROM temp_duplicates
);

DROP TEMPORARY TABLE temp_duplicates;
