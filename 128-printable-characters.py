>>> from string import (printable, digits, ascii_letters,
...                     punctuation, whitespace)
>>> digits
'0123456789'
>>> ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> whitespace
' \t\n\r\x0b\x0c'
>>> for line in wrap(printable, width=60): print(line)
...
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX
YZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
>>> digits + ascii_letters + punctuation + whitespace == printable
True