>>> def divide_numbers(*, numerator, denominator):
...     try:
...         return int(numerator)/int(denominator)
...     except ZeroDivisionError:
...         return 0
...

>>> divide_numbers(10, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: divide_numbers() takes 0 positional arguments but 2 were given

>>> divide_numbers(numerator=10, denominator=2)
5.0