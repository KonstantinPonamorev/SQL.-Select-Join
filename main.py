import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:postgre@localhost:5432/postgres')
connection = engine.connect()

select_artist_in_genre_count = connection.execute("""
    SELECT genre_name, COUNT(genre_id) FROM artist_genre
    LEFT JOIN genre ON artist_genre.genre_id = genre.id
    GROUP BY genre_name;
    """).fetchall()

select_count_tracks_20192020 = connection.execute("""
    SELECT COUNT(track_name) FROM track
    LEFT JOIN album ON track.album_id = album.id
    WHERE release_date BETWEEN 2019 AND 2020;
    """).fetchall()

select_avg_duration_by_album = connection.execute("""
    SELECT title, AVG(duration_sec) FROM track
    LEFT JOIN album ON track.album_id = album.id
    GROUP BY title;
    """).fetchall()

select_artists_not_in_2020 = connection.execute("""
    SELECT name FROM album
    LEFT JOIN artist_album ON album.id = artist_album.album_id
    LEFT JOIN artist ON artist_album.artist_id = artist.id 
    WHERE release_date NOT BETWEEN 2018 and 2018
    GROUP BY name;
    """).fetchall()

select_compilation_with_Monica = connection.execute("""
    SELECT compilation_name FROM track
    JOIN album ON track.album_id = album.id
    JOIN artist_album ON album.id = artist_album.album_id
    JOIN artist ON artist_album.artist_id = artist.id
    JOIN compilation_track ON track.id = compilation_track.track_id
    JOIN compilation ON compilation_track.compilation_id = compilation.id
    WHERE name = 'Monica Belucci'
    GROUP BY compilation_name;
    """).fetchall()

select_albums_multigenre = connection.execute("""
    SELECT title FROM album
    JOIN artist_album ON album.id = artist_album.album_id
    JOIN artist ON artist_album.album_id = artist.id
    JOIN artist_genre ON artist.id = artist_genre.artist_id
    JOIN genre ON artist_genre.genre_id = genre.id
    GROUP BY title
    HAVING COUNT(name) > 1;
    """).fetchall()

select_tracks_not_in_compilation = connection.execute("""
    SELECT track_name FROM track
    LEFT JOIN compilation_track ON track.id = compilation_track.track_id
    LEFT JOIN compilation ON compilation_track.compilation_id = compilation.id
    WHERE compilation_name = NULL;
    """).fetchall()

select_artist_shorter_track = connection.execute("""
    SELECT name FROM track
    JOIN album ON track.album_id = album.id
    JOIN artist_album ON album.id = artist_album.album_id
    JOIN artist ON artist_album.artist_id = artist.id
    WHERE duration_sec = (
        SELECT MIN(duration_sec) FROM track);
    """).fetchall()

# select_shorter_albums = connection.execute("""
#     SELECT title FROM track
#     JOIN album ON track.album_id = album.id
#     WHERE  = (
#         SELECT COUNT(title) FROM track
#         JOIN album ON track.album_id = album.id)
#     GROUP BY title;
#     """).fetchall()

# pprint(select_artist_in_genre_count)
# pprint(select_count_tracks_20192020)
# pprint(select_avg_duration_by_album)
# pprint(select_artists_not_in_2020)
# pprint(select_compilation_with_Monica)
# pprint(select_albums_multigenre)
# print(select_tracks_not_in_compilation)
# pprint(select_artist_shorter_track)