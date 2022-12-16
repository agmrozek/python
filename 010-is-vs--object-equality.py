>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> c = a
>>> a == b  # same content
True
>>> a == c  # also same content
True
>>> a is c  # same object
True
>>> a is b  # not the same object
False
# to check for equal objects you can check their
# identity using id()
>>> id(a), id(b), id(c)
(140611808855040, 140611819909632, 140611808855040)