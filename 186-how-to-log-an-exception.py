>>> import logging
>>> FORMAT = '%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s'
>>> logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO, format=FORMAT)
>>> logging.debug('not logged')
>>> logging.info('info is logged')
>>> def func(num1, num2):
...     try:
...         return num1/num2
...     except ZeroDivisionError:
...         logging.exception(f"{num1=}/{num2=} -> cannot divide by 0")
...
>>> func(1, 2)
0.5
>>> func(2, 0)
>>> ^D
$ cat example.log
2020-12-14 23:02:01,030 INFO <stdin> <module> info is logged
2020-12-14 23:03:41,510 ERROR <stdin> func num1=2/num2=0 -> cannot divide by 0
Traceback (most recent call last):
  File "<stdin>", line 3, in func
ZeroDivisionError: division by zero