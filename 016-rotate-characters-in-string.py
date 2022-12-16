>>> s = "PyBites hits 250 tips"

# rotate to the right
>>> s[3:] + s[:3]
'ites hits 250 tipsPyB'

# rotate to the left
>>> s[-3:] + s[:-3]
'ipsPyBites hits 250 t'

# you can also use deque's rotate method
>>> from collections import deque
>>> d = deque(s)
>>> d.rotate(3)
>>> d
deque(['i', 'p', 's', 'P', 'y', 'B', 'i', 't', 'e', 's', ' ', 'h', 'i', 't', 's', ' ', '2', '5', '0', ' ', 't'])
>>> "".join(d)
'ipsPyBites hits 250 t'