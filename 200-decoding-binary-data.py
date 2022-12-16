>>> import json
>>> import base64
>>> import requests

>>> url = "https://bites-data.s3.us-east-2.amazonaws.com/sales.json"
>>> response = requests.get(url)
>>> data = json.loads(response.text)

>>> data['content']
'bW9udGgsc2FsZXMNCjIwMTMtMDEtMDEsMTQyMzY...'

>>> content = base64.b64decode(data["content"])  # returns bytes
>>> for line in content.decode('utf-8').splitlines():
...     print(line)
...
month,sales
2013-01-01,14236.9
2013-02-01,4519.89
2013-03-01,55691.01
2013-04-01,28295.35
2013-05-01,23648.29
...