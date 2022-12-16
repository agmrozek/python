>>> for i in range(3):
...     '{i} apple{s}'.format(i=i, s="s" if i != 1 else "")
...
'0 apples'
'1 apple'
'2 apples'
>>> for i in range(3):
...     f'{i} apple{"s" if i != 1 else ""}'
...
'0 apples'
'1 apple'
'2 apples'