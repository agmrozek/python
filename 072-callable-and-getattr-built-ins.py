>>> import string
>>> attrs = [attr for attr in dir(string) if not attr.startswith('_')]
>>> for a in attrs: a, callable(getattr(string, a))
...
('Formatter', True)
('Template', True)
('ascii_letters', False)
…

# why getattr?
>>> attrs[0], type(attrs[0])
('Formatter', <class 'str'>)
# oops
>>> callable(attrs[0])
False
# we need to give callable the actual object:
>>> callable(getattr(string, attrs[0]))
True

# another way to check this:
>>> hasattr(string.Formatter, "__call__")
True