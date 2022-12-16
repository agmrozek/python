# credit / thanks to Ned Batchelder
>>> def chunks(lst, n):
...     """Yield successive n-sized chunks from lst."""
...     for i in range(0, len(lst), n):
...         yield lst[i:i + n]
...

# using keyword for a bit shorter output 
>>> import keyword
>>> from pprint import pprint as pp
>>> pp(list(chunks(keyword.kwlist, 5)))
[['False', 'None', 'True', '__peg_parser__', 'and'],
 ['as', 'assert', 'async', 'await', 'break'],
 ['class', 'continue', 'def', 'del', 'elif'],
 ['else', 'except', 'finally', 'for', 'from'],
 ['global', 'if', 'import', 'in', 'is'],
 ['lambda', 'nonlocal', 'not', 'or', 'pass'],
 ['raise', 'return', 'try', 'while', 'with'],
 ['yield']]