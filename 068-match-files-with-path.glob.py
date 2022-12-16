>>> from pathlib import Path

# get python files in current directory
>>> for file_path in Path('.').glob('*.py'): print(file_path)

# get python files one level deep
>>> for file_path in Path('.').glob('*/*.py'): print(file_path)

# get python files recursively (might be slow!)
>>> for file_path in Path('.').glob('**/*.py'): print(file_path)