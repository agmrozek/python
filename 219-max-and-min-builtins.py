>>> import random
>>> numbers = random.sample(range(1, 100), k=10)
>>> numbers
[32, 68, 47, 11, 36, 22, 31, 67, 27, 2]
>>> min(numbers)
2
>>> max(numbers)
68
>>> min(numbers, key=str)
11
>>> min([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: min() arg is an empty sequence
>>> min([], default=1)
1