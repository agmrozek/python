>>> text = 'a 😃 b C é 2 鞗'
>>> [(c, c.isalpha()) for c in text.split()]
[('a', True), ('😃', False), ('b', True), ('C', True), ('é', True), ('2', False), ('鞗', True)]