import logging
import subprocess

# define my own exception
class MyException(Exception):
    def __init__(self, cmd, stdout, stderr):
        super().__init__(f'{cmd} error (see stderr output for detail)')
        self.stdout = stdout
        self.stderr = stderr

# raise the exception
def run(...):
    ...
    out, err = subprocess.Popen(...)
    if err:
        raise MyException('my_command', out, err)

# catch the exception
try:
    run(...)
except MyException as exc:
    logging.error(exc.stderr)