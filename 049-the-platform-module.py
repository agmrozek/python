>>> import platform
>>> platform.machine()
'x86_64'
>>> platform.node()
'Bobs-iMac.local'

>>> platform.platform()
'Darwin-19.6.0-x86_64-i386-64bit'
>>> platform.system()
'Darwin'
>>> platform.release()
'19.6.0'

>>> platform.uname()
uname_result(system='Darwin', node='Bobs-iMac.local', release='19.6.0',
                         version='Darwin Kernel Version 19.6.0: ...
                          ... machine='x86_64', processor='i386')

>>> platform.mac_ver()
('10.15.7', ('', '', ''), 'x86_64')