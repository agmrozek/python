>>> payload = {
...   "description": "the description for this gist",
...   "public": True,
...   "files": {
...     "file1.txt": {
...       "content": "String file contents"
...     }
...   }
... }
>>> type(payload)
<class 'dict'>
>>> import json
>>> payload_json = json.dumps(payload, indent=4)
>>> type(payload_json)
<class 'str'>
>>> print(payload_json)
{
    "description": "the description for this gist",
    "public": true,
    "files": {
        "file1.txt": {
            "content": "String file contents"
        }
    }
}