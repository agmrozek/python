# given this simple package:
$ cat my_package/file_1.py
def add_two_numbers(a, b):
    return a + b

# we cannot run it as a package: 
$ python -m my_package
... No module named my_package.__main__; 'my_package' is a package and cannot be directly executed

# adding a __main__.py you can add an entry point to your package:
$ cat my_package/__main__.py
from . import file_1

def foo():
    print(file_1.add_two_numbers(3, 4))

if __name__ == '__main__':
    foo()

# now you can run the package like this:
$ python -m my_package
7