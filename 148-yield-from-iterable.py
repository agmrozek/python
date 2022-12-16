>>> def gen():
...     for i in range(1, 11):
...         yield i
...
>>> g = gen()
>>> next(g)
1
>>> next(g)
2
...
...
>>> next(g)
10
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

# same result, more concise

>>> def gen():
...     yield from range(1, 11)
...

# note that a for loop "catches" the StopIteration for you
>>> [i for i in gen()]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]