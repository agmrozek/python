>>> def mydecorator(function):
...     def wrapped(*args, **kwargs):
...         result = function(*args, **kwargs)
...         return result
...     return wrapped
...
>>> def func():
...     """ajksnd"""
...
>>> @mydecorator
... def func():
...     """my docstring"""
...     print("hello")
...
>>> func.__doc__
>>>
>>> from functools import wraps
>>> def mydecorator(function):
...     @wraps(function)  # adding this line
...     # ... rest the same ...
...
>>> @mydecorator
... def func():
...     """should be preserved now"""
...     print("hello")
...
>>> func.__doc__
'should be preserved now'