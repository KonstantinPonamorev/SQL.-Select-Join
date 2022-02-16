import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:postgre@localhost:5432/postgres')
connection = engine.connect()

# connection.execute("""DELETE FROM compilation_track""")
# connection.execute("""DELETE FROM compilation""")
# connection.execute("""DELETE FROM track""")
# connection.execute("""DELETE FROM artist_album""")
# connection.execute("""DELETE FROM album""")
# connection.execute("""DELETE FROM artist_genre""")
# connection.execute("""DELETE FROM genre""")
# connection.execute("""DELETE FROM artist""")

connection.execute("""
    INSERT INTO artist
    VALUES(1, 'Bill Murrey');
    INSERT INTO artist
    VALUES(2, 'Joe Crossby');
    INSERT INTO artist
    VALUES(3, 'Monica Belucci');
    INSERT INTO artist
    VALUES(4, 'Eddie Murphy');
    INSERT INTO artist
    VALUES(5, 'Oleg Bulygin');
    INSERT INTO artist
    VALUES(6, 'Constantine Ponamorev');
    INSERT INTO artist
    VALUES(7, 'Artist');
    INSERT INTO artist
    VALUES(8, 'You');
    """)
connection.execute("""
    INSERT INTO genre (id, genre_name)
    VALUES(1, 'HipHop');
    INSERT INTO genre
    VALUES(2, 'Pop');
    INSERT INTO genre
    VALUES(3, 'Country');
    INSERT INTO genre
    VALUES(4, 'Jazz');
    INSERT INTO genre
    VALUES(5, 'Blues');
    """)
connection.execute("""
    INSERT INTO artist_genre
    VALUES(1, 1);
    INSERT INTO artist_genre
    VALUES(1, 2);
    INSERT INTO artist_genre
    VALUES(1, 4);
    INSERT INTO artist_genre
    VALUES(2, 1);
    INSERT INTO artist_genre
    VALUES(3, 3);
    INSERT INTO artist_genre
    VALUES(3, 5);
    INSERT INTO artist_genre
    VALUES(4, 4);
    INSERT INTO artist_genre
    VALUES(4, 5);
    INSERT INTO artist_genre
    VALUES(5, 1);
    INSERT INTO artist_genre
    VALUES(5, 2);
    INSERT INTO artist_genre
    VALUES(5, 3);
    INSERT INTO artist_genre
    VALUES(5, 4);
    INSERT INTO artist_genre
    VALUES(5, 5);
    INSERT INTO artist_genre
    VALUES(6, 1);
    INSERT INTO artist_genre
    VALUES(6, 2);
    INSERT INTO artist_genre
    VALUES(6, 3);
    INSERT INTO artist_genre
    VALUES(6, 4);
    INSERT INTO artist_genre
    VALUES(6, 5);
    INSERT INTO artist_genre
    VALUES(7, 1);
    INSERT INTO artist_genre
    VALUES(7, 2);
    INSERT INTO artist_genre
    VALUES(7, 3);
    INSERT INTO artist_genre
    VALUES(8, 4);
    INSERT INTO artist_genre
    VALUES(8, 5);
    """)
connection.execute("""
    INSERT INTO album
    VALUES(1, 'If you ask me', 2018);
    INSERT INTO album
    VALUES(2, 'Broforce', 2017);
    INSERT INTO album
    VALUES(3, 'Who is', 2018);
    INSERT INTO album
    VALUES(4, 'Hope', 2022);
    INSERT INTO album
    VALUES(5, 'The best student', 2018);
    INSERT INTO album
    VALUES(6, 'Christian or Chris', 2010);
    INSERT INTO album
    VALUES(7, 'Scales', 2015);
    INSERT INTO album
    VALUES(8, 'My answer will be...', 2018);
    INSERT INTO album
    VALUES(9, 'Last Dance', 2017);
    INSERT INTO album
    VALUES(10, 'Lost in yourself', 2020);
    INSERT INTO album
    VALUES(11, 'Me', 2018);
    """)
connection.execute("""
    INSERT INTO artist_album
    VALUES(1, 2);
    INSERT INTO artist_album
    VALUES(1, 4);
    INSERT INTO artist_album
    VALUES(2, 2);
    INSERT INTO artist_album
    VALUES(2, 4);
    INSERT INTO artist_album
    VALUES(3, 6);
    INSERT INTO artist_album
    VALUES(4, 7);
    INSERT INTO artist_album
    VALUES(5, 1);
    INSERT INTO artist_album
    VALUES(5, 3);
    INSERT INTO artist_album
    VALUES(5, 5);
    INSERT INTO artist_album
    VALUES(5, 8);
    INSERT INTO artist_album
    VALUES(5, 11);
    INSERT INTO artist_album
    VALUES(6, 1);
    INSERT INTO artist_album
    VALUES(6, 3);
    INSERT INTO artist_album
    VALUES(6, 5);
    INSERT INTO artist_album
    VALUES(6, 8);
    INSERT INTO artist_album
    VALUES(6, 11);
    """)
connection.execute("""
    INSERT INTO track
    VALUES(1, 'Question 1', 137, 1);
    INSERT INTO track
    VALUES(2, 'Question 2', 149, 1);
    INSERT INTO track
    VALUES(3, 'Question 3', 150, 1);
    INSERT INTO track
    VALUES(4, 'My Bro', 200, 2);
    INSERT INTO track
    VALUES(5, 'Not My Bro', 187, 2);
    INSERT INTO track
    VALUES(6, '...I am', 176, 3);
    INSERT INTO track
    VALUES(7, '...kill Kenny', 182, 3);
    INSERT INTO track
    VALUES(8, 'Just a little Hope', 324, 4);
    INSERT INTO track
    VALUES(9, 'For a little man', 350, 5);
    INSERT INTO track
    VALUES(10, 'In the ugly World', 290, 5);
    INSERT INTO track
    VALUES(11, 'Just C', 196, 6);
    INSERT INTO track
    VALUES(12, 'One Line', 182, 7);
    INSERT INTO track
    VALUES(13, 'Yes', 168, 8);
    INSERT INTO track
    VALUES(14, 'No', 168, 8);
    INSERT INTO track
    VALUES(15, 'Rumba', 178, 9);
    INSERT INTO track
    VALUES(16, 'I will find you', 187, 10);
    INSERT INTO track
    VALUES(17, 'Forget me', 174, 10);
    INSERT INTO track
    VALUES(18, 'Constantine', 196, 11);
    INSERT INTO track
    VALUES(19, 'Ponamorev', 196, 11);
    """)
connection.execute("""
    INSERT INTO compilation
    VALUES(1, 'For your soul', 2019);
    INSERT INTO compilation
    VALUES(2, 'Relax', 2019);
    INSERT INTO compilation
    VALUES(3, 'Training', 2021);
    INSERT INTO compilation
    VALUES(4, 'Car', 2022);
    INSERT INTO compilation
    VALUES(5, 'Street', 2022);
    INSERT INTO compilation
    VALUES(6, 'Alone', 2021);
    INSERT INTO compilation
    VALUES(7, 'Party', 2020);
    INSERT INTO compilation
    VALUES(8, 'NonStop', 2019);
    """)
connection.execute("""
    INSERT INTO compilation_track
    VALUES(1, 2);
    INSERT INTO compilation_track
    VALUES(1, 4);
    INSERT INTO compilation_track
    VALUES(2, 6);
    INSERT INTO compilation_track
    VALUES(2, 10);
    INSERT INTO compilation_track
    VALUES(3, 2);
    INSERT INTO compilation_track
    VALUES(3, 10);
    INSERT INTO compilation_track
    VALUES(3, 1);
    INSERT INTO compilation_track
    VALUES(4, 7);
    INSERT INTO compilation_track
    VALUES(4, 8);
    INSERT INTO compilation_track
    VALUES(5, 5);
    INSERT INTO compilation_track
    VALUES(5, 9);
    INSERT INTO compilation_track
    VALUES(6, 1);
    INSERT INTO compilation_track
    VALUES(6, 3);
    INSERT INTO compilation_track
    VALUES(6, 8);
    INSERT INTO compilation_track
    VALUES(7, 2);
    INSERT INTO compilation_track
    VALUES(7, 4);
    INSERT INTO compilation_track
    VALUES(7, 6);
    INSERT INTO compilation_track
    VALUES(7, 8);
    INSERT INTO compilation_track
    VALUES(8, 3);
    INSERT INTO compilation_track
    VALUES(8, 5);
    INSERT INTO compilation_track
    VALUES(8, 7);
    INSERT INTO compilation_track
    VALUES(8, 9);
    INSERT INTO compilation_track
    VALUES(8, 11);
    """)

# sel = connection.execute("""
#     SELECT * FROM artist;
#     """).fetchall()
# sel_2 = connection.execute("""
#     SELECT * FROM genre;
#     """).fetchall()
# sel_3 = connection.execute("""
#     SELECT * FROM artist_genre;
#     """).fetchall()
# sel_4 = connection.execute("""
#     SELECT * FROM album;
#     """).fetchall()
# sel_5 = connection.execute("""
#     SELECT * FROM artist_album;
#     """).fetchall()
# sel_6 = connection.execute("""
#     SELECT * FROM track;
#     """).fetchall()
# sel_7 = connection.execute("""
#     SELECT * FROM compilation;
#     """).fetchall()
# sel_8 = connection.execute("""
#     SELECT * FROM compilation_track;
#     """).fetchall()
#
#
# pprint(sel)
# pprint(sel_2)
# pprint(sel_3)
# pprint(sel_4)
# pprint(sel_5)
# pprint(sel_6)
# pprint(sel_7)
# pprint(sel_8)
