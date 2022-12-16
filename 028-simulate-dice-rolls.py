>>> import itertools
>>> import random
>>> dice = range(1, 7)
>>> list(dice)
[1, 2, 3, 4, 5, 6]

>>> combinations = list(itertools.product(dice, repeat=2))  # random.choice below needs a list
>>> len(combinations)
36
>>> combinations[:5]  # use slicing to get a little sample
[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]

>>> for _ in range(3):
...     random.choice(combinations)
...
(2, 6)
(1, 4)
(5, 6)
>>> random.sample(combinations, 5)
[(6, 2), (2, 4), (6, 1), (4, 2), (4, 3)]