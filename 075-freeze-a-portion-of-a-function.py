>>> from functools import partial
>>> print_no_newline = partial(print, end=', ')
>>> for _ in range(3): print('test')
...
test
test
test
>>> for _ in range(3): print_no_newline('test')
...
test, test, test, >>>