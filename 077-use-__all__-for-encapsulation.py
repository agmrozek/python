$ more mod.py
__all__ = ['a', 'b']

def a():
    pass

def b():
    pass

def c():
    pass

$ python
>>> from mod import *
>>>
>>> a()
>>> b()
>>> c()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined