$ python3.7

>>> a = 1
>>> b = 'julian'
>>> c = [2, 3, 4]
>>> f"{a=} {b=} {c=}"
  File "<fstring>", line 1
    (a=)
      ^
SyntaxError: invalid syntax

$ python3.8

>>> a = 1
>>> b = 'julian'
>>> c = [2, 3, 4]
>>> f"{a=} {b=} {c=}"
"a=1 b='julian' c=[2, 3, 4]"