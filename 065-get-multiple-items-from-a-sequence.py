>>> from operator import itemgetter

>>> days = ['mon', 'tue', 'wed', 'thurs', 'fri', 'sat', 'sun']
>>> f = itemgetter(3, 6)
>>> f(days)
('thurs', 'sun')

# same as:
>>> days.__getitem__(3), days.__getitem__(6)
('thurs', 'sun')

# works with strings too:
>>> f("hello world")
('l', 'w')

# using with dict keys and in one go:
>>> workouts
{'mon': 'chest+biceps', 'tue': 'legs', 'wed': 'cardio', 'thurs': 'back+triceps', 'fri': 'legs', 'sat': 'rest', 'sun': 'rest'}
>>> itemgetter('mon', 'tue')(workouts)
('chest+biceps', 'legs')