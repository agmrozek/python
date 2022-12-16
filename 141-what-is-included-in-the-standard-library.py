>>> from stdlib_list import stdlib_list
>>> libs_39 = stdlib_list("3.9")
>>> len(libs_39)
334

>>> libs_39[:5]
['__future__', '__main__', '_thread', 'abc', 'aifc']
>>> libs_39[-5:]
['zipapp', 'zipfile', 'zipimport', 'zlib', 'zoneinfo']

>>> libs_38 = stdlib_list("3.8")
>>> set(libs_39) - set(libs_38)
{'test.support.bytecode_helper', 'zoneinfo', 'graphlib', 'test.support.socket_helper'}

>>> libs_37 = stdlib_list("3.7")
>>> libs_36 = stdlib_list("3.6")
>>> 'dataclasses' in (set(libs_37) - set(libs_36))
True