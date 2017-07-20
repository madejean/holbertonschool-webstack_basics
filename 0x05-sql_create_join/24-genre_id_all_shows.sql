SELECT tv_shows.title, tv_show_genres.genre_id from tv_shows
LEFT JOIN tv_show_genres on tv_shows.id = show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
