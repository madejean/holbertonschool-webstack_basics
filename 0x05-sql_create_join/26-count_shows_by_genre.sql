SELECT tv_genres.name, COUNT(tv_genres.name) as number_shows from tv_genres
LEFT JOIN tv_show_genres on tv_genres.id = genre_id
GROUP BY tv_genres.name
ORDER BY  number_shows DESC;
