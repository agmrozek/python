>>> s = """pybites "code challenges" community "data science" development"""

# split on space won't work
>>> s.split()
['pybites', '"code', 'challenges"', 'community', '"data', 'science"', 'development']

# enter shlex
>>> import shlex
>>> shlex.split(s)
['pybites', 'code challenges', 'community', 'data science', 'development']

# if it was not for shlex
>>> import re
>>> [element.strip('"') for element in re.findall(r'"[^"]*"|[^"\W]+', s)]
['pybites', 'code challenges', 'community', 'data science', 'development']