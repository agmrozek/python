import random

# make it predictable
>>> random.seed(12)
>>> random.sample([1,2,3,4,5], 2)
[4, 3]
>>> random.sample([1,2,3,4,5], 2)
[5, 3]
>>> random.sample([1,2,3,4,5], 2)
[2, 4]

# same results
>>> random.seed(12)
>>> random.sample([1,2,3,4,5], 2)
[4, 3]
>>> random.sample([1,2,3,4,5], 2)
[5, 3]
>>> random.sample([1,2,3,4,5], 2)
[2, 4]