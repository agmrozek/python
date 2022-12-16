>>> import os
>>> from pathlib import Path
>>> import shutil
>>> homework = Path("homework")
>>> os.makedirs(homework)
>>> for i in range(1, 4):
...     open(homework / f"file{i}", 'w').close()
...
>>> os.listdir(homework)
['file3', 'file2', 'file1']
>>> homework2 = Path("homework2")
>>> shutil.copytree(homework, homework2)
PosixPath('homework2')
>>> os.listdir(homework2)
['file3', 'file2', 'file1']
>>> shutil.rmtree(homework2)  # be very careful with this command, it doesn't ask you first!
>>> homework2.is_dir()
False
# some other fun ones (all use os under the hood)
>>> shutil.which("python3")
'/Library/Frameworks/Python.framework/Versions/3.9/bin/python3'
>>> shutil.disk_usage("/")  # os.statvfs
usage(total=1027680514048, used=15045521408, free=324004749312)
>>> shutil.get_terminal_size()  # os.get_terminal_size
os.terminal_size(columns=114, lines=37)