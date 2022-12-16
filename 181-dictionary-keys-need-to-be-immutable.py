>>> a = (1, 2, 3)  # tuple with immutable types
>>> b = (1, [], 2)  # spoiler: this tuple contains a mutable object
>>> d = dict()
>>> d[a] = 1
>>> d
{(1, 2, 3): 1}
>>> d[b] = 2
...
TypeError: unhashable type: 'list'

# another example
>>> a = set([1,2,3])
>>> d = {}
>>> d[a] = 1
...
TypeError: unhashable type: 'set'
>>> aa = frozenset(a)
>>> aa
frozenset({1, 2, 3})
>>> d[aa] = 1
>>>