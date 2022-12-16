>>> class WithoutSlots:
...     def __init__(self, x, y, z):
...         self.x = x
...         self.y = y
...         self.z = z
...
>>> class WithSlots:
...     __slots__ = 'x', 'y', 'z'
...     def __init__(self, x, y, z):
...         self.x = x
...         self.y = y
...         self.z = z
...
>>> from pympler.asizeof import asizeof  # pip install
>>> w1 = WithoutSlots(1, 2, 3)
>>> w2 = WithSlots(4, 5, 6)
>>> asizeof(w1)
416
>>> asizeof(w2)
152
>>> w1.a = 1
>>> w2.a = 1
...
AttributeError: 'WithSlots' object has no attribute 'a'