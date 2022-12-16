>>> class Ninja:
...     def __init__(self):
...         self._score = 0
...
...     @property
...     def score(self):
...         return self._score
...
...     @score.setter
...     def score(self, new_score):
...         if new_score < 0:
...             raise ValueError('Score cannot be negative')
...         self._score = new_score
...
>>> n = Ninja()
>>> n.score
0
>>> n.score = 2
>>> n.score = -1
...
ValueError: Score cannot be negative
>>> n.score
2