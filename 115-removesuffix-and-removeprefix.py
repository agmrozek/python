>>> "this is PyBites".strip("PyBites")
'his is '  # oops
>>> "this is PyBites".removesuffix("PyBites")
'this is '
>>> "pybites shares tips".strip("pybites")
' shares '  # oops
>>> "pybites shares tips".removeprefix("pybites")
' shares tips'