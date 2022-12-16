>>> from textwrap import wrap

>>> text = ("Every great developer you know got there by solving "
...         "problems they were unqualified to solve until they "
...         "actually did it. - Patrick McKenzie")

>>> for line in wrap(text, width=80): print(line)
...
Every great developer you know got there by solving problems they were
unqualified to solve until they actually did it. - Patrick McKenzie

>>> for line in wrap(text, width=40): print(line)
...
Every great developer you know got there
by solving problems they were
unqualified to solve until they actually
did it. - Patrick McKenzie