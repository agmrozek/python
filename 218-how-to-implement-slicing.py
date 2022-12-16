>>> class A:
...     def __init__(self, items):
...         self._items = items
...
>>> a = A([1,2,3])
>>> a[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'A' object is not subscriptable
>>> class A:
...     def __init__(self, items):
...         self._items = items
...     def __getitem__(self, index):
...         return self._items[index]
...
>>> a = A([1,2,3])
>>> a[0]
1
>>> a[-1]
3
>>> a[1:]
[2, 3]