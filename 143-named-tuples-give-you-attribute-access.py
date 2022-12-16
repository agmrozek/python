>>> from collections import namedtuple
>>> from datetime import date
>>> Transaction = namedtuple('Transaction', 'giver points date')
>>> tr = Transaction('tim', 5, date.today())
# or: Transaction(giver='tim', points=5, date=date.today())
>>> tr
Transaction(giver='tim', points=5, date=datetime.date(2020, 11, 14))
>>> tr[0]
'tim'
>>> tr.giver
'tim'
>>> tr.points
5
>>> tr.points = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute