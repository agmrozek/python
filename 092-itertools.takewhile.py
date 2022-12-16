>>> ninja_belts
{10: 'white', 50: 'yellow', 100: 'orange', 175: 'green', 250: 'blue', 400: 'brown', 
 600: 'black', 800: 'paneled', 1000: 'red'}
>>> from itertools import takewhile
>>> def get_belts(user_score):
...     return takewhile(lambda x: x[0] <= user_score,
...             ninja_belts.items())
...
>>> for i in (7, 18, 51, 174, 176):
...     i, list(get_belts(i))
...
(7, [])
(18, [(10, 'white')])
(51, [(10, 'white'), (50, 'yellow')])
(174, [(10, 'white'), (50, 'yellow'), (100, 'orange')])
(176, [(10, 'white'), (50, 'yellow'), (100, 'orange'), (175, 'green')])