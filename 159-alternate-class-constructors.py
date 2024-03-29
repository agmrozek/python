>>> from datetime import datetime, date
>>> class MyDate:
...
...     def __init__(self, year, month, day):
...         self.date = date(year, month, day)
...
...     @classmethod
...     def from_str(cls, date_str):
...         year, month, day = date_str.split("-")
...         return cls(int(year), int(month), int(day))
...
>>> d1 = MyDate(2016, 12, 19)
>>> d1.date
datetime.date(2016, 12, 19)

# an alternative way to instantiate a MyDate object:
>>> d2 = MyDate.from_str("2016-12-19")
>>> d2.date
datetime.date(2016, 12, 19)
>>> d1.date == d2.date
True