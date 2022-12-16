>>> from dataclasses import dataclass
>>> @dataclass
... class Bite:
...     number: int
...     title: str
...     level: str = 'Beginner'
...
...     def __post_init__(self):
...         self.title = self.title.capitalize()
...
>>> bite = Bite(1, "sum n numbers")
>>> repr(bite)
"Bite(number=1, title='Sum n numbers', level='Beginner')"
>>> bite.level = 2  # dataclasses are mutable
>>> bite
Bite(number=1, title='Sum n numbers', level=2)
# make an immutable dataclass
>>> @dataclass(frozen=True)
... class Bite:
...     # same but without __post_init__ (dataclasses.FrozenInstanceError)

>>> bite = Bite(1, "sum n numbers")
>>> bite.level = 2
...
dataclasses.FrozenInstanceError: cannot assign to field 'level'