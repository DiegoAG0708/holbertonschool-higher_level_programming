-- Task 9: Cities by States
-- This script lists all cities with their state names, ordered by city id

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
