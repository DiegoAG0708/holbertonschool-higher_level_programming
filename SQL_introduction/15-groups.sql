-- Task 15: Number by score
-- This script lists each score and the number of records with that score, sorted by count descending
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
