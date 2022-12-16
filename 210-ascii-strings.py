>>> s, t = "python", "très bien"

# use ord
>>> def is_ascii(word):
...     return all(ord(char) < 128 for char in word)
...
>>> is_ascii(s), is_ascii(t)
(True, False)

# another way
>>> t.encode()
b'tr\xc3\xa8s bien'
>>> t.encode('ascii', errors='ignore')
b'trs bien'
>>> len(t.encode('ascii', errors='ignore')) < len(t)
True

# now you can use isascii though (>= Python 3.7)
>>> s.isascii(), t.isascii()
(True, False)