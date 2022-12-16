$ python -V
Python 3.6.0

$ python3.9 -V
Python 3.9.0

>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=0, releaselevel='final', serial=0)
>>> sys.version_info.major
3
>>> if sys.version_info.major < 3: print("Python 3 only please!")
...
>>> if (sys.version_info.major, sys.version_info.minor) < (3, 9):
...     print("Use Python 3.9")
...
Use Python 3.9