# full code: https://gist.github.com/pybites/6a15bfe006057b6d82e85b4fd1240beb
import concurrent.futures
import os
import requests

def _download_page(url):
    fname = os.path.basename(url)
    r = requests.get(url)
    with open(f'downloads/{fname}', 'wb') as outfile:
        outfile.write(r.content)

def download_urls_sequentially(urls):
    for url in urls:
        _download_page(url)

def download_urls_concurrently(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
        future_to_url = {executor.submit(_download_page, url): url
                         for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            future_to_url[future]

$ time python dl.py -s
real	0m51.322s

$ time python dl.py -c
real	0m2.878s