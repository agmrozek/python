>>> import itertools
>>> lights = itertools.cycle('Red Green Amber'.split())
>>> next(lights)
'Red'
>>> next(lights)
'Green'
>>> next(lights)
'Amber'
>>> next(lights)
'Red'
>>> next(lights)
'Green'
>>> next(lights)
'Amber'