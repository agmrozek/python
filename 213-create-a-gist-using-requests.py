import json

from decouple import config  # pip install python-decouple
import requests

TOKEN = config('GITHUB_TOKEN')

def create_gist(filename, description, code, public=True):
    payload = json.dumps({
        "description": description,
        "public": public,
        "files": {
            filename: {"content": code}
        }
    })
    gists_url = "https://api.github.com/gists"
    headers = {'Authorization': f'token {TOKEN}'}
    resp = requests.post(gists_url, data=payload, headers=headers)
    resp.raise_for_status()
    return resp.json()['html_url']