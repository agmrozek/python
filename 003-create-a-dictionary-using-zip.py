>>> names = 'bob julian tim sara'.split()
>>> ages = '11 22 33 44'.split()
>>> zip(names, ages)
<zip object at 0x7fae75920d20>
>>> list(zip(names, ages))
[('bob', '11'), ('julian', '22'), ('tim', '33'), ('sara', '44')]
>>> dict(zip(names, ages))
{'bob': '11', 'julian': '22', 'tim': '33', 'sara': '44'}