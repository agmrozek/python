>>> tweets = ("I was happy with the book", "this is awful",
...           "Python is object oriented", "Python is awesome")

>>> print('\n'.join(tweets))
I was happy with the book
this is awful
Python is object oriented
Python is awesome

>>> print(' >> '.join(tweets))
I was happy with the book >> this is awful >> Python is object oriented >> Python is awesome

# make sure all elements are strings

>>> '-'.join([100, 'pybites', 'tips', 4, 'you'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 0: expected str instance, int found

>>> '-'.join(str(w) for w in [100, 'pybites', 'tips', 4, 'you'])
'100-pybites-tips-4-you'