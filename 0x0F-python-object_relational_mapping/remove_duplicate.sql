#!/usr/bin/node

USE hbtn_0e_0_usa;
DELETE FROM states
WHERE id NOT IN (
  SELECT MIN(id)
  FROM (SELECT * FROM states) AS tmp
  GROUP BY name
);
