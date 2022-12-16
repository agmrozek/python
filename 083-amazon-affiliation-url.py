>>> import os
>>> import re
>>> import pyperclip
>>> def gen_affiliation_link(url):
...     if not re.search(r"amazon.*/dp/", url):
...         raise ValueError(f"{url} is not a valid Amazon product link")
...     asin = re.sub(r".*/dp/([^/]+).*", r"\1", url)
...     code = os.environ.get("AMAZON_AFFILIATE_CODE", "pyb0f-20")
...     return f"http://www.amazon.com/dp/{asin}/?tag={code}"
...
>>> def copy_affiliation_link():
...     url = pyperclip.paste()
...     link = gen_affiliation_link(url)
...     pyperclip.copy(link)
...
# going to Amazon, we copy this link to our clipboard:
# https://www.amazon.com/Pragmatic-Programmer-journey-mastery-Anniversary
# /dp/0135957052/ref=sr_1_1?dchild=1&keywords=pragmatic+programmer&sr=8-1
# then we call
>>> copy_affiliation_link()
# which sends this generated affiliation URL back to our clipboard: 
# http://www.amazon.com/dp/0135957052/?tag=pyb0f-20