# initial code
from pathlib import Path
from tempfile import TemporaryDirectory

# tree.py > https://gist.github.com/pybites/248d6190c27defc3b832ca6cef9ac495
from tree import count_dirs_and_files

def test_only_files():
    with TemporaryDirectory(dir="/tmp") as dirname:
        for i in range(1, 6):
            filename = f'{i}.txt'
            path = Path(dirname) / filename
            with open(path, 'w') as f:
                f.write('hello')
        assert count_dirs_and_files(dirname) == (0, 5)

# refactored using pytest's tmp_path fixture
def test_only_files_refactored(tmp_path):
    for i in range(1, 6):
        path = tmp_path / f'{i}.txt'
        with open(path, 'w') as f:
            f.write('hello')
    assert count_dirs_and_files(tmp_path) == (0, 5)