-- Find cities linked to California
SELECT id,name FROM cities WHERE state_id = 1
ORDER BY cities.id ASC;
