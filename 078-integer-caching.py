>>> a = [5, 200, 256, 257, 300, 500]
>>> b = [5, 200, 256, 257, 300, 500]
>>> for i, j in zip(a, b):
...   print(i, j, i is j)
...
5 5 True
200 200 True
256 256 True
257 257 False
300 300 False
500 500 False