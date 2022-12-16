>>> a = 'hello'
>>> type(a)
<class 'str'>
>>> str.__mro__
(<class 'str'>, <class 'object'>)
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__' ...]
>>> help(a.strip)
Help on built-in function strip:

strip(...) method of builtins.str instance
    S.strip([chars]) -> str
...