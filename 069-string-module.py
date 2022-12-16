>>> import random
>>> import string

>>> ''.join(random.choice(string.ascii_lowercase) for i in range(20))
'jjkjsgyksqfmtgpujmud'

# "sample" seems more adequate:
>>> ''.join(random.sample(string.ascii_lowercase + string.digits, 20))
'oytkq3u4l6hnbpz19r85'

# other constants you can use:
>>> help(string)
...
DATA
    __all__ = ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'cap...
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    whitespace = ' \t\n\r\x0b\x0c'