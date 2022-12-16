>>> names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
>>> countries = 'Australia Spain Global Argentina'.split()

# truncation - oops!
>>> list(zip(names, countries))
[('Julian', 'Australia'), ('Bob', 'Spain'), ('PyBites', 'Global'), ('Dante', 'Argentina')]

# adding None to shortest iterator = countries
>>> from itertools import zip_longest
>>> list(zip_longest(names, countries))
[('Julian', 'Australia'), ('Bob', 'Spain'), ('PyBites', 'Global'), ('Dante', 'Argentina'), ('Martin', None), ('Rodolfo', None)]

# same but with a fillvalue other than None
>>> list(zip_longest(names, countries, fillvalue="Worldwide"))
[('Julian', 'Australia'), ('Bob', 'Spain'), ('PyBites', 'Global'), ('Dante', 'Argentina'), ('Martin', 'Worldwide'), ('Rodolfo', 'Worldwide')]