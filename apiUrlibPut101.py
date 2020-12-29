#!/usr/bin/env python

import urllib.request
import json
url = "http://localhost:8080/v1/books"
book = {
    "name": "The Art of Computer Programming",
    "authors": ["Donald Knuth"],
    "date": 1968,
    "isbn": "0-201-03801-3"
}
payload = json.dumps(book).encode('utf8')
request = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
response = urllib.request.urlopen(request)
print(response.status)
