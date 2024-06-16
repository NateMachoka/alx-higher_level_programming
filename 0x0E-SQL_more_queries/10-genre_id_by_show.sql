-- Lists all tv shows in a database
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_shows.genre ON tv_shows.id=tv_shows_genre.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
