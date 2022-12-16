>>> from contextlib import contextmanager
>>> import sqlite3

>>> @contextmanager
... def connect_db():
...     try:
...         conn = sqlite3.connect('movies.db')
...         conn.row_factory = sqlite3.Row  # fetchall returns dicts
...         yield conn.cursor()
...     finally:
...         conn.commit()
...         conn.close()
...
>>> movies = [('Inception', 2010, 'Christopher Nolan', 8.8),
...           ('The Shawshank Redemption', 1994, 'Frank Darabont', 9.2),
...           ('Heat', 1995, 'Michael Mann', 8.2)]

>>> with connect_db() as cursor:
...     cursor.execute("CREATE TABLE movies (title, year, director, rating)")
...     cursor.executemany('INSERT INTO movies VALUES (?,?,?,?)', movies)
...     movies = cursor.execute("SELECT * FROM movies WHERE year > 2000;")
...     first = movies.fetchall()[0]
...     dict(first)
...
# omitting "<sqlite3.Cursor object at ... " standard output
{'title': 'Inception', 'year': 2010, 'director': 'Christopher Nolan', 'rating': 8.8}