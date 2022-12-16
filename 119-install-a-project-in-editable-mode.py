# hm… my package is not in my path
>>> import sys
>>> [p for p in sys.path if p.endswith('pbreadinglist')]
[]

# creating a minimal setup.py (this is not enough for PyPI of course)
(venv) $ more setup.py
import setuptools
setuptools.setup(name='pbreadinglist', version='1.0')
# now I can install it in editable mode
(venv) $ pip install --editable .
# alternatively add this to your requirements.txt
-e .
...

# now I got this in my virtual environment
$ more venv/lib/python3.8/site-packages/pbreadinglist.egg-link
/Users/bobbelderbos/code/pbreadinglist
.
# and voila, my current directory is in my path now
>>> import sys
>>> [p for p in sys.path if p.endswith('pbreadinglist')]
['/Users/bobbelderbos/code/pbreadinglist']