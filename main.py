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


# pprint(select_artist_in_genre_count)
# pprint(select_count_tracks_20192020)
# pprint(select_avg_duration_by_album)