>>> names = ['dana', 'tim', 'sara', 'ana', 'joyce', 'dana', 'tim', 'ana']

>>> set(names)
{'tim', 'joyce', 'dana', 'ana', 'sara'}

>>> {name.title() for name in names if "a" in name}
{'Ana', 'Dana', 'Sara'}