>>> def sum_numbers(number, all_numbers=[]):
...     all_numbers.append(number)
...     return sum(all_numbers)
...
>>> sum_numbers(1, [2, 3])
6
>>> sum_numbers(1)
1
>>> sum_numbers(2)  # oops, should return 2!
3
>>> def sum_numbers(number, all_numbers=None):
...     if all_numbers is None:
...         all_numbers = []
...     all_numbers.append(number)
...     return sum(all_numbers)
...
>>> sum_numbers(1)
1
# ok now
>>> sum_numbers(2)
2
>>> sum_numbers(3)
3