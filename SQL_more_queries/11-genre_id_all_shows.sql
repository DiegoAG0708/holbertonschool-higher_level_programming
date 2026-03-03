-- Task 11: Genre ID for all shows
-- This script lists all shows with their genre IDs, showing NULL if no genre exists

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
