>>> from operator import attrgetter
>>> class Person:
...     def __init__(self, name, age, profession):
...         self.name = name
...         self.age = age
...         self.profession = profession

>>> jane = Person("Jane Goodall", 86, "primatologist")
>>> attrgetter('name')(jane)
'Jane Goodall'

# get multiple attributes
>>> ag = attrgetter('name', 'age', 'profession')
>>> ag(jane)
('Jane Goodall', 86, 'primatologist')

# only works for valid attributes
>>> attrgetter('name2')(jane)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Person' object has no attribute 'name2'