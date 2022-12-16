>>> from collections import defaultdict
>>> data = """Tim,ID
... Sara,BR
... Thelma,CN
... Chris,RU
... Fina,ID
... Juliana,SE
... Roberto,CN
... Mario,PL
... Paul,CN"""
>>> countries = defaultdict(list)
>>> for line in data.splitlines():
...     name, country_code = line.split(',')
...     countries[country_code].append(name)
...
>>> countries
defaultdict(<class 'list'>,
            {'BR': ['Sara'], 'CN': ['Thelma', 'Roberto', 'Paul'],
             'ID': ['Tim', 'Fina'], 'PL': ['Mario'],
             'RU': ['Chris'], 'SE': ['Juliana']})