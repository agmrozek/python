# dl.py
...
from timeit import timeit

URLS = 'urls'

# code from previous tip ...

if __name__ == '__main__':
    with open(URLS) as f:
        urls = [u.rstrip() for u in f.readlines()]
        funcs = 'download_urls_sequentially, download_urls_concurrently'
        for func in funcs.split(', '):
            print(func)
            print(timeit(f"{func}(urls)",
                         f"from __main__ import {funcs}, urls",
                         number=1))

$ python dl.py
download_urls_sequentially
53.683453743
download_urls_concurrently
2.6830952339999996