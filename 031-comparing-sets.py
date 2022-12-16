>>> a = {1, 2, 3, 4, 5}  # or use set() on a list
>>> b = {1, 2, 3, 6, 7, 8}
# unique to a
>>> a - b
{4, 5}
# unique to b
>>> b - a
{8, 6, 7}
# in both sets
>>> a & b
{1, 2, 3}
# in either one or the other
>>> a ^ b
{4, 5, 6, 7, 8}
# no need for more verbose (and probably slower) looping
>>> line1 = ['You', 'can', 'do', 'anything', 'but', 'not', 'everything']
>>> line2 = ['We', 'are', 'what', 'we', 'repeatedly', 'do']
>>> for word in line1:
...     if word in line2: print(word)
...
do
>>> set(line1) & set(line2)
{'do'}