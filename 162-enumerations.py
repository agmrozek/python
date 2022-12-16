>>> from enum import Enum, IntEnum
>>> class BiteLevel(Enum):
...     INTRO = 1
...     BEGINNER = 2
...     INTERMEDIATE = 3
...     ADVANCED = 4
...
>>> print(repr(BiteLevel.BEGINNER))
<BiteLevel.BEGINNER: 2>
>>> adv = BiteLevel.ADVANCED
>>> adv.name, adv.value
('ADVANCED', 4)
>>> for name, member in BiteLevel.__members__.items(): name, member
...
('INTRO', <BiteLevel.INTRO: 1>)
('BEGINNER', <BiteLevel.BEGINNER: 2>)
...
# Do you want to compare to integers? Use IntEnum
>>> BiteLevel.INTRO == 1
False
>>> class SpecialLevel(IntEnum):
...    ...
>>> SpecialLevel.INTRO == 1
True