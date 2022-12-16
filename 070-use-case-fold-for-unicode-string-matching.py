>>> a, b = "der Fluß", "der Fluss"

>>> a.lower() == b.lower()
False

# casefold converts 'ß' "ss" which makes the 2 strings identical
>>> a.casefold() == b.casefold()
True

>>> 'ß'.casefold()
'ss'