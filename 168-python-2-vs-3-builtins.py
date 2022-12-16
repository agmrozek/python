# the following line is from a python 2.7 REPL session
# if you want to try it you might need to pip install the "future" library
>>> py2_builtins = ['ArithmeticError', ..., 'xrange', 'zip']

# python 3.9
>>> import builtins
>>> from pprint import pprint as pp
>>> py3_builtins = dir(builtins)
>>> pp(set(py2_builtins) - set(py3_builtins))
{... 'absolute_import',
 'apply',
 'basestring',
 'buffer',
 'cmp',
 'coerce',
 'execfile',
 'file',
 'intern',
 'long',
 'raw_input',
 'reduce',
 'reload',
 'sys',
 'unichr',
 'unicode',
 'xrange'}