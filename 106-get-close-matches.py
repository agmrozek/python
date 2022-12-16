>>> from difflib import get_close_matches
>>> names = ['julian', 'pybites', 'bob', 'tim', 'python', 'sara', 'james', 'ana']
>>> get_close_matches('pythonista', names)
['python']
>>> get_close_matches('pybit', names)
['pybites']
>>> get_close_matches('jul', names)
['julian']
>>> get_close_matches('ara', names)
['sara', 'ana']