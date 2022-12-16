>>> from urllib.request import urlretrieve

>>> url = ("https://pybites-tips.s3.eu-central-1.amazonaws.com/"
...        "python-download-file.png")

>>> urlretrieve(url)
('/var/folders/r1/p3qtn9t55tvdz8t1l47jhpgc0000gn/T/tmpu2ui82tl', 
 <http.client.HTTPMessage object at 0x7fc60a5a1d00>)
>>> urlretrieve(url, 'localfile.png')
('localfile.png', <http.client.HTTPMessage object at 0x7fc60a5a1190>)

>>> import requests
>>> r = requests.get(url)
>>> with open("localfile2.png", "wb") as f:
...     f.write(r.content)
...
200032