# using pdb to have my cars json (source: Mockeroo) loaded into the data list
(Pdb) from collections import Counter, defaultdict
(Pdb) from pprint import pprint as pp
(Pdb) pp data
[{'automaker': 'Dodge', 'id': 1, 'model': 'Ram Van 1500', 'year': 1999},
 {'automaker': 'Chrysler', 'id': 2, 'model': 'Town & Country', 'year': 2002},
 {'automaker': 'Porsche', 'id': 3, 'model': 'Cayenne', 'year': 2008},
... many more records ...

(Pdb) cars = defaultdict(lambda: Counter())  # or: defaultdict(functools.partial(Counter))
(Pdb) for row in data: cars[row["automaker"]][row["model"]] += 1
(Pdb) pp cars
defaultdict(<function <lambda> at 0x7fe3aaa22f70>,
            {'Acura': Counter({'CL': 3,
                               'NSX': 3,
                               'RL': 3,
                               'Vigor': 2,
        ...
             'Audi': Counter({'A8': 4,
                              'TT': 4,
        ...
                              'Q7': 1,
                              'A3': 1}),
        ...
        ... many more ...