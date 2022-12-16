>>> import importlib
>>> import inspect

>>> module = importlib.import_module('random')  # or __import__('random')
>>> sample = getattr(module, 'sample')

>>> sample([1, 2, 3, 4, 5], 2)
[1, 3]

>>> inspect.getsource(sample)[:50]
'    def sample(self, population, k, *, counts=None'