>>> from collections import namedtuple
>>> from datetime import date
>>> import keyword
>>> import pickle

>>> Transaction = namedtuple('Transaction', 'giver points date')
>>> tr = Transaction(giver='tim', points=5, date=date.today())
>>> class MyClass:
...     def is_keyword(self, name):
...             return keyword.iskeyword(name)
...
>>> mc = MyClass()
>>> mc.is_keyword('None')
True
>>> with open('data.pkl', 'wb') as outfile:  # note the b
...     pickle.dump(tr, outfile)
...     pickle.dump(mc, outfile)
...
>>> with open('data.pkl', 'rb') as infile:  # again note the b
...     tr = pickle.load(infile)
...     mc = pickle.load(infile)
...
>>> tr
Transaction(giver='tim', points=5, date=datetime.date(2020, 12, 17))
>>> mc.is_keyword('None')
True