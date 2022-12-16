>>> "first line\r\nsecond line".split("\n")
['first line\r', 'second line']

# includes \r (Carriage Return) in the splitting
>>> "first line\r\nsecond line".splitlines()
['first line', 'second line']

>>> "first line\rsecond line".splitlines()
['first line', 'second line']

>>> "first line\nsecond line".splitlines()
['first line', 'second line']