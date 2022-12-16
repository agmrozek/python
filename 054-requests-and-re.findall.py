>>> import re
>>> import requests 
>>> html = requests.get('https://pybit.es/archives.html').text

>>> matches = re.findall(r'https://pybit\.es/guest.*?\.html', html)
>>> len(matches)
29
>>> for m in matches: print(m)
...
https://pybit.es/guest-create-aws-lambda-layers.html
https://pybit.es/guest-clean-text-data.html
...
...
https://pybit.es/guest-learning-apis.html
https://pybit.es/guest-making-of-task-manager.html