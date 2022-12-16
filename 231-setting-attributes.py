>>> s = "name: PyBites\norigin: Worldwide\nborn: 2016-12-19"
>>> class MyClass:
...     pass
...
>>> mc1 = MyClass()
>>> for line in s.splitlines():
...     key, value = line.split(": ")
...     mc1.key = value
...
# oops!
>>> [attr for attr in mc1.__dir__() if not attr.startswith('__')]
['key']
# the proper way:
>>> mc2 = MyClass()
>>> for line in s.splitlines():
...     key, value = line.split(": ")
...     setattr(mc2, key, value)
...
>>> [attr for attr in mc2.__dir__() if not attr.startswith('__')]
['name', 'origin', 'born']
>>> mc2.name, mc2.origin, mc2.born
('PyBites', 'Worldwide', '2016-12-19')