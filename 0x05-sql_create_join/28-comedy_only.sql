-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title as title from tv_shows
INNER JOIN tv_show_genres on tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres on  tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name ="Comedy"
ORDER BY tv_shows.title;
