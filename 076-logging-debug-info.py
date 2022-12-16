>>> import logging
>>> try:
...     1/0
... except ZeroDivisionError:
...     logging.exception("message")
...
ERROR:root:message
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero