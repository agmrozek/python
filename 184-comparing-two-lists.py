>>> import difflib
>>> julian_todos = ["1. Be awesome.", "2. Pybites.", "3. Enjoy a beer."]
>>> bob_todos = ["1. Be awesome!", "2. PyBites.", "3. Enjoy a beer."]
>>> for jtodo, btodo in zip(julian_todos, bob_todos):
...     if jtodo != btodo:
...         print(f"< {jtodo}\n> {btodo}")
...
< 1. Be awesome.
> 1. Be awesome!
< 2. Pybites.
> 2. PyBites.
# There must be a better way for this?! Yes! Enter difflib:
>>> for line in difflib.Differ().compare(julian_todos, bob_todos):
...     print(line)
...
- 1. Be awesome.
?              ^

+ 1. Be awesome!
?              ^

- 2. Pybites.
?      ^

+ 2. PyBites.
?      ^

  3. Enjoy a beer.