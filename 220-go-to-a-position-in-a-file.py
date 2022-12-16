>>> content = "line 1\nline 2\nline 3\nline 4\n"
>>> with open("file1.txt", "w") as f:
...     f.write(content.strip())
...
27
>>> with open("file1.txt", "r") as f:
...     f.readline()
...     f.tell()
...     f.seek(0)
...     f.tell()
...     f.readline()
...     f.seek(15)
...     f.read()
...
'line 1\n'
7
0
0
'line 1\n'
15
'ine 3\nline 4'