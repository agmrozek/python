$ cat ~/bin/pystartup.py
import os
from pprint import pprint as pp
import sys

sys.path.append(os.path.join(os.path.expanduser("~"), 'bin'))

$ export PYTHONSTARTUP=~/bin/pystartup.py

# this script should be importable now
$ ls ~/bin/c*py
/Users/bobbelderbos/bin/chaining.py

$ python3
>>> pp(dir('a string'))  # pp is available
['__add__',
 '__class__',
 '__contains__',
...
>>> sys.path[-1]
'/Users/bobbelderbos/bin'
>>> import chaining  # works as importable from ~/bin