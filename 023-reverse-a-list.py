>>> numbers = [1, 2, 3, 4, 5]
# in-place
>>> numbers.reverse()
>>> numbers
[5, 4, 3, 2, 1]
>>> list(reversed(numbers))
[1, 2, 3, 4, 5]
>>> numbers
[5, 4, 3, 2, 1]
>>> numbers[::-1]
[1, 2, 3, 4, 5]