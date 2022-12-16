# let's subclass a list, a better way:
# https://treyhunner.com/2019/04/why-you-shouldnt-inherit-from-list-and-dict-in-python/

>>> from collections import UserList
>>> class MyList(UserList):
...     pass
...
>>> my_list = MyList()
>>> MyList.__mro__
(<class '__main__.MyList'>, <class 'collections.UserList'>, 
<class 'collections.abc.MutableSequence'>, <class 'collections.abc.Sequence'>,
<class 'collections.abc.Reversible'>, <class 'collections.abc.Collection'>,
<class 'collections.abc.Sized'>, <class 'collections.abc.Iterable'>,
<class 'collections.abc.Container'>, <class 'object'>)

# isinstance = faster and considers inheritance
>>> type(my_list)
<class '__main__.MyList'>
>>> from collections.abc import Sequence
>>> type(my_list) is Sequence
False
>>> isinstance(my_list, Sequence)
True
>>> isinstance(my_list, object)
True