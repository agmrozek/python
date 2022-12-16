>>> workouts = {
...     "Mon": "upper body 1",
...     "Tue": "lower body 1",
... }
>>> workouts.setdefault("Mon", "new workout")
'upper body 1'
>>> workouts
{'Mon': 'upper body 1', 'Tue': 'lower body 1'}
>>> workouts.setdefault("Wed", "new workout")
'new workout'
>>> workouts
{'Mon': 'upper body 1', 'Tue': 'lower body 1', 'Wed': 'new workout'}