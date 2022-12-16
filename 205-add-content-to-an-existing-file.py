>>> with open('file', 'w') as f:
...     f.write("some content\n")
...
13
>>> with open('file', 'r') as f:
...     f.readlines()
...
['some content\n']
>>> with open('file', 'w') as f:
...     f.write("some other content\n")
...
19
>>> with open('file', 'r') as f:
...     f.readlines()
...
['some other content\n']  # oops
>>> with open('file', 'a') as f:
...     f.write("appending new content\n")
...
22
>>> with open('file', 'r') as f:
...     f.readlines()
...
['some other content\n', 'appending new content\n']