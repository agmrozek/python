>>> import urllib.request as req

# oops
>>> url = 'https://pybit.es'
>>> req.urlopen(url).read()
...403

# more work
>>> r = req.Request(url)
>>> r.add_header('User-agent','wswp')

>>> req.urlopen(r).status
200

# requests abstracts all this away
>>> import requests
>>> requests.get(url).status_code
200