>>> import keyword
>>> import builtins

>>> keyword.kwlist
['False', 'None', 'True', ..., 'with', 'yield']
>>> len(keyword.kwlist)
36

>>> keyword.iskeyword('file')
False
>>> keyword.iskeyword('if')
True
>>> keyword.iskeyword('locals')
False
>>> keyword.iskeyword('nonlocal')
True

>>> 'locals' in dir(builtins)
True
>>> 'property' in dir(builtins)
True

>>> set(dir(builtins)) & set(keyword.kwlist)
{'None', 'False', 'True'}
>>> None = 10
...
SyntaxError: cannot assign to None