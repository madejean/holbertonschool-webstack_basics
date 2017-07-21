-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each other
SELECT tv_genres.name as genre, COUNT(tv_genres.name) as number_shows FROM tv_genres
LEFT JOIN tv_show_genres on tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_shows DESC;