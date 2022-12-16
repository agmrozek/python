>>> color = 'yellow'

# is this a primary color?
>>> color == 'red' or color == 'blue' or color == 'yellow'  # don't do this
True

>>> primary_colors = set(['red', 'yellow', 'blue'])
>>> color in primary_colors
True