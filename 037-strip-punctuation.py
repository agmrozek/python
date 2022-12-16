>>> from string import punctuation
>>> punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# use string methods:
>>> my_string = "punc;tu.ation!"
>>> table = str.maketrans({key: None for key in punctuation})
>>> my_string.translate(table)
'punctuation'

# or use a comprehension:
>>> ''.join(c for c in my_string if c not in punctuation)
'punctuation'