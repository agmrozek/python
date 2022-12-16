>>> import subprocess

>>> cmd = 'git log -5 --oneline'
>>> output = subprocess.check_output(cmd, shell=True).splitlines()

>>> output_lines = [line.decode() for line in output]
>>> print(*output_lines, sep='\n')
9e61a85 Fix nox temp error on windows (#69)
db4f571 refactor tests - separate files and conftest.py for fixtures (#61)
e705392 fix #51 - avoids compiling by using psycopg2-binary (#67)
c93168f Feature notes - users can store public and private notes
bc654f7 Merge pull request #66 from pmayd/poetry_and_conda