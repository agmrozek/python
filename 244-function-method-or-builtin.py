>>> import inspect
>>> import random
>>> class A:
...     def my_method(self):
...         pass
...
>>> a = A()
>>> def func():
...     pass
...
>>> for obj in random.sample, inspect.isbuiltin, any, a.my_method, func, A:
...     if inspect.isfunction(obj):
...         print(f"{obj.__name__} is a function.")
...     elif inspect.ismethod(obj):
...         print(f"{obj.__name__} is a method.")
...     elif inspect.isbuiltin(obj):
...         print(f"{obj.__name__} is a builtin.")
...     else:
...         print(f"I don't know what {obj.__name__} is")
...
sample is a method.
isbuiltin is a function.
any is a builtin.
my_method is a method.
func is a function.
I don't know what A is