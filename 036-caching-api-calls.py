>>> import requests
>>> import requests_cache

# supported backends: sqlite (default), mongodb, redis, memory
# expiring cache in 10 seconds for example sake

>>> requests_cache.install_cache('cache.db', backend='sqlite', expire_after=10)

>>> resp = requests.get("https://pybit.es/")
>>> resp.from_cache
False
>>> resp = requests.get("https://pybit.es/")
>>> resp.from_cache
True

# waiting for 15 seconds
>>> resp = requests.get("https://pybit.es/")
>>> resp.from_cache
False
# request straight after last one, using cache again
>>> resp = requests.get("https://pybit.es/")
>>> resp.from_cache
True