-- Displays number of shows linked to each genre and filters those without
SELECT name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
