>>> s = "hello world from pybites"
>>> s[:5] == "hello"  # no need
True
>>> s.startswith("hello")
True
>>> s[-2:] == 'es'
True
# better:
>>> s.endswith('es')
True

# optional args
>>> s.startswith("from")
False
>>> s[12:]
'from pybites'
>>> s.startswith("from", 12)
True

>>> s[:-8]
'hello world from'
>>> s.endswith("from", 0, -8)
True

# tuples are supported too:
>>> t = "hello world from spain"
>>> s.endswith(("pybites", "spain"))
True
>>> t.endswith(("pybites", "spain"))
True