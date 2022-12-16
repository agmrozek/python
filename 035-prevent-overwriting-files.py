>>> with open('hello', 'w') as f:
...     f.write('hello')
...
5

$ more hello
hello

>>> with open('hello', 'w') as f:
...     f.write('spam')
...
4

# oops

$ more hello
spam

# 'x' prevents this:
 
>>> with open('hello', 'x') as f:
...     f.write('spam')
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileExistsError: [Errno 17] File exists: 'hello'