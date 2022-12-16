>>> ll =  ['Hello1', 'pyth0n', 'coding']
>>> sorted(ll)
['Hello1', 'coding', 'pyth0n']

>>> sorted(ll, key=lambda x: any(s.isdigit() for s in x))
['coding', 'Hello1', 'pyth0n']

# What if we also want to sort the digits? Use a helper:
>>> import re
>>> def get_digit(s):
...     m = re.search(r"(\d+)", s)
...     return int(m.group()) if m else -1
...

>>> ll = ['python', 'py4you', 'coding', 'pyth0n', 'Hello3', 'hello1']
>>> sorted(ll, key=get_digit)
['python', 'coding', 'pyth0n', 'hello1', 'Hello3', 'py4you']