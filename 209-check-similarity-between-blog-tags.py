>>> from itertools import combinations
>>> from difflib import SequenceMatcher

>>> tags = 'python pythonista developer development'.split()

>>> for pair in combinations(tags, 2):
...     similarity = SequenceMatcher(None, *pair).ratio()
...     print(pair, similarity)
...
('python', 'pythonista') 0.75
('python', 'developer') 0.13333333333333333
('python', 'development') 0.23529411764705882
('pythonista', 'developer') 0.10526315789473684
('pythonista', 'development') 0.19047619047619047
('developer', 'development') 0.8