# pip install xmltodict
>>> import xmltodict
>>> xml = '''<?xml version="1.0" encoding="UTF-8"?>
... <root response="True">
...   <movie title="The Prestige" year="2006" released="20 Oct 2006" runtime="130 min" />
...   <movie title="The Dark Knight" year="2008" released="18 Jul 2008" runtime="152 min" />
...   <movie title="Interstellar" year="2014" released="07 Nov 2014" runtime="169 min" />
... </root>'''

# convert xml to dict
>>> movies = xmltodict.parse(xml)
>>> type(movies)
<class 'collections.OrderedDict'>

# retrieve titles and years
>>> for m in movies['root']['movie']:
...     print(m['@title'], m['@year'])
...
The Prestige 2006
The Dark Knight 2008
Interstellar 2014