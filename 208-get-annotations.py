>>> def hello(name: str) -> str:
...     return f"Hello {name}"
...
>>> hello.__annotations__
{'name': <class 'str'>, 'return': <class 'str'>}

# no return
>>> def hello(name: str):
...     pass
...
>>> hello.__annotations__
{'name': <class 'str'>}

# another example
>>> from typing import List  # Python < 3.9
>>> def print_names_to_columns(names: List[str], cols: int = 2) -> None:
...     """A function to print names to N columns"""
...
>>> print_names_to_columns.__annotations__
{'names': typing.List[str], 'cols': <class 'int'>, 'return': None}