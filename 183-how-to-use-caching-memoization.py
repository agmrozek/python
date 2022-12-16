>>> from functools import lru_cache
>>> from timeit import timeit

>>> def nocache_fib(n):
...     if n < 2:
...         return n
...     return nocache_fib(n - 1) + nocache_fib(n - 2)
...

>>> @lru_cache
... def cached_fib(n):
...     if n < 2:
...         return n
...     return cached_fib(n - 1) + cached_fib(n - 2)
...

>>> timeit("nocache_fib(40)", "from __main__ import nocache_fib", number=1)
38.08430259900001
>>> timeit("cached_fib(40)", "from __main__ import cached_fib", number=1)
6.163200009723369e-05