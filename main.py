import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:postgre@localhost:5432/postgres')
connection = engine.connect()

select_artist_in_genre_count = connection.execute("""
    SELECT genre_name, COUNT(genre_id) FROM artist_genre
    LEFT JOIN genre ON artist_genre.genre_id = genre.id
    GROUP BY genre_name;
    """).fetchall()


# pprint(select_artist_in_genre_count)