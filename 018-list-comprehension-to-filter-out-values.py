>>> languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']
>>> [l for l in languages if l.lower().startswith('p')]
['Python', 'Perl', 'PHP', 'Python', 'Python']

# alternative but less readable

>>> list(filter(lambda l: l.lower().startswith('p'), languages))
['Python', 'Perl', 'PHP', 'Python', 'Python']