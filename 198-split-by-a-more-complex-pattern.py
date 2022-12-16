>>> import re
>>> lines = """
... Inception,2010;Christopher Nolan|8.8
... The Shawshank Redemption;1994|Frank Darabont?9.2
... Heat^1995[Michael Mann]8.2
... """

>>> for line in lines.strip().splitlines():
...     re.split(r'[^\w\s\.]', line)
...
['Inception', '2010', 'Christopher Nolan', '8.8']
['The Shawshank Redemption', '1994', 'Frank Darabont', '9.2']
['Heat', '1995', 'Michael Mann', '8.2']

# or to not repeat the regex pattern inside the loop:
>>> pat = re.compile(r'[^\w\s\.]')
>>> for line in lines.strip().splitlines():
...     re.split(pat, line)
...
['Inception', '2010', 'Christopher Nolan', '8.8']
['The Shawshank Redemption', '1994', 'Frank Darabont', '9.2']
['Heat', '1995', 'Michael Mann', '8.2']