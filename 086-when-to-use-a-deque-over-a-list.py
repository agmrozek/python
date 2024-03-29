>>> from collections import deque
>>> import random
>>> from timeit import timeit

>>> lst = list(range(10_000_000))
>>> deq = deque(range(10_000_000))

>>> def insert_and_delete(ds):
...     for _ in range(10):
...         index = random.choice(range(100))
...         ds.remove(index)
...         ds.insert(index, index)

# wow
>>> timeit("insert_and_delete(lst)", "from __main__ import insert_and_delete, lst", number=10)
1.6085020060000375
>>> timeit("insert_and_delete(deq)", "from __main__ import insert_and_delete, deq", number=10)
0.00024063900002602168