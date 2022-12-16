(venv) $ python manage.py dumpdata books.Book > books.json

# REPL
>>> import json
>>> from pprint import pprint as pp
>>> with open('books.json') as f:
...     books = json.loads(f.read())
...
>>> type(books)
<class 'list'>
>>> first_book = books[0]
>>> pp(first_book)
{'fields': {'added': '2020-11-27T15:29:23.924Z',
            'authors': 'Gary Keller',
            'cover': 'https://images-na.ssl-images-amazon.com/images/I/31bLXJwHXlL._SX344_BO1,204,203,200_.jpg',
            'description': 'The One Thing explains the success habit to ...',
            'link': 'https://www.amazon.com/ONE-Thing-Surprisingly-Extraordinary-Results/dp/1885167776',
            'page_count': 240,
            'publisher': 'John Murray Press',
            'title': 'The One Thing'},
 'model': 'books.book',
 'pk': 1}