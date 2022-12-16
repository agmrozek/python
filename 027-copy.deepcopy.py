>>> from copy import copy, deepcopy
>>> items = [dict(id=1, name='laptop')]
>>> items2 = copy(items)
>>> items[0]['name'] = 'macbook'
>>> items
[{'id': 1, 'name': 'macbook'}]
>>> items2
[{'id': 1, 'name': 'macbook'}]  # oops!

>>> items = [dict(id=1, name='laptop')]
>>> items2 = deepcopy(items)
>>> items[0]['name'] = 'macbook'
>>> items
[{'id': 1, 'name': 'macbook'}]
>>> items2
[{'id': 1, 'name': 'laptop'}]  # this object stays intact as per intention