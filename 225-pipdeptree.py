(venv) $ pip show requests
...
Requires: chardet, urllib3, certifi, idna
Required-by: tinys3, social-auth-core, requests-oauthlib, PyGithub

# pipdeptree gives more info:
(venv) $ pipdeptree -p requests
requests==2.25.1
  - certifi [required: >=2017.4.17, installed: 2020.6.20]
  - chardet [required: >=3.0.2,<5, installed: 3.0.4]
...

# list the tree in reverse = what other project dependencies are using requests?
(venv) $ pipdeptree -r -p requests
requests==2.25.1
  - PyGithub==1.54.1 [requires: requests>=2.14.0]
  - requests-oauthlib==1.3.0 [requires: requests>=2.0.0]
...

# it even warns you about conflicting dependencies:
(venv) $ pipdeptree -p Django
Warning!!! Possibly conflicting dependencies found:
* Django==3.1.5
 - sqlparse [required: >=0.2.2, installed: 0.1.0]