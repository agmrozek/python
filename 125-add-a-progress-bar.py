import concurrent.futures
import os

import requests
from tqdm import tqdm

def _download_page(url):
    …

def download_urls_concurrently(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
        future_to_url = {executor.submit(_download_page, url): url
                         for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            # make this a generator for tqdm
            yield future_to_url[future]

if __name__ == '__main__':
    with open(URLS) as f:
        urls = [u.rstrip() for u in f.readlines()]

        # all you need to do is wrap an iterable with tqdm, sweet!
        for _ in tqdm(download_urls_concurrently(urls), total=len(urls)):
            pass

$ python dl.py
100%|███████████████████████| 228/228 [00:02<00:00, 83.07it/s]