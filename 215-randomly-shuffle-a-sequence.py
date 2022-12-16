>>> from collections import namedtuple
>>> from pprint import pprint as pp
>>> import random

>>> Card = namedtuple('Card', ['value', 'suit'])
>>> suits = ['hearts', 'diamonds', 'spades', 'clubs']
>>> cards = [Card(value, suit) for value in range(1, 14) for suit in suits]
>>> pp(cards[:3])
[Card(value=1, suit='hearts'),
 Card(value=1, suit='diamonds'),
 Card(value=1, suit='spades')]
>>> random.shuffle(cards)

# shuffled in place
>>> pp(cards[:3])
[Card(value=13, suit='clubs'),
 Card(value=1, suit='spades'),
 Card(value=2, suit='spades')]