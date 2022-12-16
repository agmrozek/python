>>> languages = ['Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Ruby']
>>> all(len(l) >= 2 for l in languages)
True
>>> any('++' in l for l in languages)
True