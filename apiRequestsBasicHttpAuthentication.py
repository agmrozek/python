#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth
import json
import sys

url = "http://localhost:8080/v1/accounts"
username = 'admin'
password = 'w0FimhVrty1ck9Pf2UAK4luOnkEgrDvy1VEK9iZsZOk='
accounts = requests.get(url, auth=HTTPBasicAuth(username, password))

try:
    accounts.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("Error: {}".format(e))
    sys.exit()

print(accounts.status_code)
