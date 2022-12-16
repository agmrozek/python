>>> def gen_subjects():
...     while True:
...         yield "Keep your Python muscles strong"
...         yield ("You have not redeemed any Bite Exercises in a while, "
...                "get back on track!")
...         yield "You still have Bite Exercises to claim!"
...
>>> abc_subjects = gen_subjects()
>>> for _ in range(8):
...     next(abc_subjects)
...
'Keep your Python muscles strong'
'You have not redeemed any Bite Exercises in a while, get back on track!'
'You still have Bite Exercises to claim!'
'Keep your Python muscles strong'
'You have not redeemed any Bite Exercises in a while, get back on track!'
'You still have Bite Exercises to claim!'
'Keep your Python muscles strong'
'You have not redeemed any Bite Exercises in a while, get back on track!'