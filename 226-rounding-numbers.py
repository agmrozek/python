>>> numbers = [0.5, 1.5, 2.5]
>>> for num in numbers:
...     num, round(num)
...
(0.5, 0)
(1.5, 2)
(2.5, 2)  # rounds "half even" aka "bankers rounding"
>>> import math
>>> for num in numbers:
...     num, math.floor(num), math.ceil(num)
...
(0.5, 0, 1)
(1.5, 1, 2)
(2.5, 2, 3)
>>> from decimal import Decimal, getcontext, ROUND_FLOOR
>>> getcontext().rounding = ROUND_FLOOR  # default ROUND_HALF_EVEN
>>> for num in numbers:
...     num, Decimal(num).quantize(Decimal("1"))
...
(0.5, Decimal('0'))
(1.5, Decimal('1'))
(2.5, Decimal('2'))