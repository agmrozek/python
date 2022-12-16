>>> numbers = [[1], [2, 3], [4, [5, 6, [7, 8, [9, [10, 11, 12]]]]]]

>>> from itertools import chain
>>> list(chain.from_iterable(numbers))
[1, 2, 3, 4, [5, 6, [7, 8, [9, [10, 11, 12]]]]]

>>> def flatten(numbers):
...     for num in numbers:
...         if isinstance(num, int):
...             yield num
...         else:
...             yield from flatten(num)
...

>>> flatten(numbers)
<generator object flatten at 0x7fae0b17b510>

>>> list(flatten(numbers))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
>>> sum(flatten(numbers))
78