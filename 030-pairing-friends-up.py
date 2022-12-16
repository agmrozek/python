>>> import itertools
>>> friends = 'bob tim julian fred'.split()
>>> list(itertools.combinations(friends, 2))
[('bob', 'tim'), ('bob', 'julian'), ('bob', 'fred'), ('tim', 'julian'), ('tim', 'fred'), ('julian', 'fred')]

>>> list(itertools.permutations(friends, 2))
[('bob', 'tim'), ('bob', 'julian'), ('bob', 'fred'), ('tim', 'bob'), ('tim', 'julian'), ('tim', 'fred'), ('julian', 'bob'), ('julian', 'tim'), ('julian', 'fred'), ('fred', 'bob'), ('fred', 'tim'), ('fred', 'julian')]