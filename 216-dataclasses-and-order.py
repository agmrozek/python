>>> from dataclasses import dataclass
>>> from enum import IntEnum

>>> class BiteLevel(IntEnum):  # supports comparing integers
...     BEGINNER = 2
...     INTERMEDIATE = 3
...     ADVANCED = 4
...
>>> @dataclass
... class Bite:
...     number: int
...     title: str
...     level: int = BiteLevel.BEGINNER
...
>>> bites = [
...     Bite(11, "Enrich a class", BiteLevel.ADVANCED),
...     Bite(21, "Query a nested DS", BiteLevel.BEGINNER),
...     Bite(25, "No promo twice", BiteLevel.INTERMEDIATE),
... ]
>>> sorted(bites)
...
TypeError: '<' not supported between instances of 'Bite' and 'Bite'

>>> @dataclass(order=True)  # now comparison works out of the box