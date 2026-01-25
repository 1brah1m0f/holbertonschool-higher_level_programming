-- Genre_id All Shows
SELECT show1.title, genre.genre_id FROM tv_shows show1 LEFT JOIN tv_show_genres genre ON show1.id = genre.show_id ORDER BY show1.title ASC, genre.genre_id ASC;