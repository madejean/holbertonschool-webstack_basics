SELECT tv_shows.title as title, tv_genres.name as name from tv_shows
LEFT JOIN tv_show_genres on tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres on tv_genres.id = genre_id
ORDER BY title, name;
