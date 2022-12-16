# range = iterable / lazy
>>> range(1, 11)
range(1, 11)
# so casting to list
# also note upper bound is exclusive
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 3rd arg = stepping
>>> list(range(1, 11, 2))
[1, 3, 5, 7, 9]
# reverse
>>> list(range(11, 1))
[]
# use negative step
>>> list(range(11, 1, -1))
[11, 10, 9, 8, 7, 6, 5, 4, 3, 2]