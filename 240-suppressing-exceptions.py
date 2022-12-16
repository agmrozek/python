>>> import os
>>> from contextlib import suppress
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> with suppress(ZeroDivisionError):
...     1/0
...
# from docs
>>> os.remove('someotherfile.tmp')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'someotherfile.tmp'
>>> with suppress(FileNotFoundError):
...     os.remove('someotherfile.tmp')
...