>>> domains = ["pybit.es", "codechalleng.es", "shop.pybit.es", "something.longer.pybit.es"]

# hm this gives me different sized lists
>>> [domain.split(".") for domain in domains]
[['pybit', 'es'], ['codechalleng', 'es'], ['shop', 'pybit', 'es'], ['something', 'longer', 'pybit', 'es']]

# rpartition for the win:
>>> [domain.rpartition(".") for domain in domains]
[('pybit', '.', 'es'), ('codechalleng', '.', 'es'), ('shop.pybit', '.', 'es'), ('something.longer.pybit', '.', 'es')]

# to clean up the dot you can also split from the end
>>> [domain.rsplit(".", 1) for domain in domains]
[['pybit', 'es'], ['codechalleng', 'es'], ['shop.pybit', 'es'], ['something.longer.pybit', 'es']]