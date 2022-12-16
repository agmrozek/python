>>> from functools import wraps, partial
>>> import requests
>>> def retry(func=None, *, times=3):
...     if func is None:
...         # https://pybit.es/articles/decorator-optional-argument/
...         return partial(retry, times=times)
...     @wraps(func)  # should always do
...     def wrapper(*args, **kwargs):
...         attempt = 0
...         while attempt < times:
...             try:
...                 return func(*args, **kwargs)
...             except Exception as exc:
...                 attempt += 1
...                 print(f"Exception {func}: {exc} (attempt: {attempt})")
...         print(f"{attempt} times tried with no success")
...         return None
...     return wrapper
...
>>> @retry(times=2)
... def get(url):
...     resp = requests.get(url)
...     resp.raise_for_status()
...
>>> get('https://httpbin.org/status/200')  # ok
>>> get('https://httpbin.org/status/404')  # tries max 2 times

Exception <function get at 0x10a6c6ef0>: 404 Client Error: NOT FOUND for url: https://httpbin.org/status/404 (attempt: 1)
Exception <function get at 0x10a6c6ef0>: 404 Client Error: NOT FOUND for url: https://httpbin.org/status/404 (attempt: 2)
2 times tried with no success