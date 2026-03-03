-- Task 16: Say my name
-- This script lists all records with a non-empty name from second_table, ordered by score descending
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name != '' 
ORDER BY score DESC;
