>>> from itertools import groupby
>>> from operator import itemgetter
>>> cars = [
...     ('Toyota', 'Avalon'), ('Ford', 'Bronco'),
...     ('Chevrolet', 'Cavalier'), ('Chevrolet', 'Corvette'),
...     ('Volkswagen', 'GTI'), ('Toyota', 'Highlander'),
...     ('Chevrolet', 'Impala'), ('Nissan', 'Maxima'),
...     ('Ford', 'Mustang'), ('Kia', 'Optima'),
...     ('Volkswagen', 'Passat'), ('Nissan', 'Pathfinder'),
...     ('Ford', 'Taurus'), ('Nissan', 'Titan'),
... ]
>>> cars.sort()  # required
>>> for manufacturer, models in groupby(cars, key=itemgetter(0)):
...     print(f'* {manufacturer}')
...     print(", ".join(model[1] for model in models))
...
* Chevrolet
Cavalier, Corvette, Impala
* Ford
Bronco, Mustang, Taurus
… …
* Volkswagen
GTI, Passat