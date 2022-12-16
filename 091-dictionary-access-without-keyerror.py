>>> workouts = {
...   "Mon": "upper body 1",
...   "Tue": "lower body 1",
...   "Thu": "upper body 2",
...   "Fri": "lower body 2"
... }
>>> workouts['Mon']
'upper body 1'
>>> workouts['Fri']
'lower body 2'
>>> workouts['Sat']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Sat'
>>> ret = workouts.get('Sat')
>>> ret is None
True
>>> workouts.get('Sat', 'not a workout day')
'not a workout day'