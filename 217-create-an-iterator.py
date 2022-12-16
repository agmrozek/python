>>> class Halving:
...     def __init__(self, start):
...         self.number = start
...     def __iter__(self):
...         return self
...     def __next__(self):
...         self.number /= 2
...         if self.number < 10:
...             raise StopIteration
...         return self.number
...
>>> ha = Halving(50)
>>> next(ha)
25.0
>>> next(ha)
12.5
>>> next(ha)
...
StopIteration
>>> for number in Halving(50):
...     print(number)
...
25.0
12.5