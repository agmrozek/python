>>> import itertools
>>> seq = itertools.count(11)
>>> next(seq)
11
>>> next(seq)
12

# with step
>>> seq = itertools.count(6, step=3)
>>> for _ in range(3):
...     next(seq)
...
6
9
12

>>> seq = itertools.count(3.75, step=0.25)
>>> for _ in range(3):
...     next(seq)
...
3.75
4.0
4.25