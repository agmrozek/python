>>> from bisect import insort

>>> items = [3, 5, 7]

>>> insort(items, 6)
>>> items
[3, 5, 6, 7]

>>> insort(items, 4)
>>> items
[3, 4, 5, 6, 7]

>>> insort(items, 9)
>>> items
[3, 4, 5, 6, 7, 9]

>>> insort(items, 20)
>>> items
[3, 4, 5, 6, 7, 9, 20]

>>> insort(items, 15)
>>> items
[3, 4, 5, 6, 7, 9, 15, 20]