>>> from abc import ABCMeta, abstractmethod

>>> class Developer(metaclass=ABCMeta):
...     @abstractmethod
...     def get_post_days(self):
...         """Subclasses of Developer must implement this method"""
...
>>> class Julian(Developer):
...     pass
...
# oops
>>> jul = Julian()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Julian with abstract method get_post_days

>>> class Julian(Developer):
...     def get_post_days(self):
...         return 'Tue Wed'.split()
...
# ok
>>> jul = Julian()
>>>