$ python3.8
>>> def greet_all(names: list[str]) -> None:
...     for name in names:
...         print("Hello", name)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
>>> from typing import List
>>> def greet_all(names: List[str]) -> None:
...     pass
...
>>> ^D
$ python3.9
>>> def greet_all(names: list[str]) -> None:
...     for name in names:
...         print("Hello", name)
...
>>>