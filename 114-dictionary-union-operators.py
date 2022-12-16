>>> dict1 = {'a': 10, 'b': 5, 'c': 3}
>>> dict2 = {'d': 6, 'c': 4, 'b': 8}

# not the "obvious way" to merge two dicts
>>> {**dict1, **dict2} 
{'a': 10, 'b': 8, 'c': 4, 'd': 6}

# 3.9 now supports union operators
# returning new dict
>>> dict1 | dict2
{'a': 10, 'b': 8, 'c': 4, 'd': 6}
>>> dict2 | dict1
{'d': 6, 'c': 3, 'b': 5, 'a': 10}

# or modifying in-place
>>> dict1
{'a': 10, 'b': 5, 'c': 3}
>>> dict1 |= dict2
>>> dict1
{'a': 10, 'b': 8, 'c': 4, 'd': 6}