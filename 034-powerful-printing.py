>>> row = ["1", "bob", "developer", "python"]

>>> print(','.join(str(x) for x in row))
1,bob,developer,python

>>> print(*row, sep=',')
1,bob,developer,python