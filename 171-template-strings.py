>>> from string import Template
>>> s = Template("Hey $name, congratulations on your $belt Ninja Belt")
>>> s.substitute(name="Tim", belt="Orange")
'Hey Tim, congratulations on your Orange Ninja Belt'
>>> s = Template("$name, your balance is $$ $amount")  # escape $
>>> s.substitute(name="Julian", amount=10000)
'Julian, your balance is $ 10000'

# by default need to substitute all
>>> s.substitute(name="Julian")
Traceback (most recent call last):
...
KeyError: 'amount'
# if you want to allow for partial replacements
>>> s = s.safe_substitute(name="Julian")
>>> s
'Julian, your balance is $ $amount'

# works with files too (activate.sh has: source $venv_path/bin/activate)
>>> with open('activate.sh') as f:
...     Template(f.readline().strip()).substitute(venv_path='venv')
...
'source venv/bin/activate'