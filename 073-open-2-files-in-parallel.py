$ more f1.txt
a
f
g
s
s

$ more f2.txt
a
scseww
sa
23
saf

>>> with open('f1.txt') as f1, open('f2.txt') as f2:
...     for i, j in zip(f1, f2):
...             print(f'{i.strip()}={j.strip()}')
...
a=a
f=scseww
g=sa
s=23
s=saf