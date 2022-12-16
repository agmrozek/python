# example from libgravatar
>>> base_url = "{protocol}://{domain}/avatar/{hash}{extension}{params}"

>>> params_dict = {
...     'protocol': 'https',
...     'domain': 'secure.gravatar.com',
...     'hash': '5b13356d467af88631503c27a3d0e0cf',
...     'extension': '.jpg',
...     'params': '?somevar=1'
... }

>>> base_url.format(**params_dict)
'https://secure.gravatar.com/avatar/5b13356d467af88631503c27a3d0e0cf.jpg?somevar=1'