>>> from pathlib import Path
>>> tmp = Path('/tmp')
>>> countries = tmp / 'countries.xml'  # before: os.path.join
>>> countries.exists()  # before: os.path.exists
True
>>> countries.is_dir()
False