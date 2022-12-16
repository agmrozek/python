>>> from getpass import getpass, getuser
>>> from inspect import getsource
>>> import os
>>> from pprint import pprint as pp

>>> username = input('Enter your username: ')
Enter your username: bob
>>> password = getpass('Enter your password: ')
Enter your password:
>>> username, password
'bob', 'password'

>>> getuser()
'bobbelderbos'
>>> os.environ['LOGNAME']
'bobbelderbos'

>>> pp(getsource(getuser))
...
 "    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):\n"
 '        user = os.environ.get(name)\n'
 '        if user:\n'
 '            return user\n'
...