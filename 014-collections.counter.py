>>> from collections import Counter
>>> languages = 'Python Java Perl Python JS C++ JS Python'.split()
>>> Counter(languages)
Counter({'Python': 3, 'JS': 2, 'Java': 1, 'Perl': 1, 'C++': 1})
>>> Counter(languages).most_common(2)
[('Python', 3), ('JS', 2)]