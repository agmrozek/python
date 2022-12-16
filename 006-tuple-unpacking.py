>>> url = ('https://www.amazon.com/War-Art-Through-Creative-Battles'
...        '/dp/1936891026/?keywords=war+of+art')

>>> url.split('/')
['https:', '', 'www.amazon.com', 'War-Art-Through-Creative-Battles', 'dp', '1936891026', '?keywords=war+of+art']

>>> url.split('/')[2:-1]
['www.amazon.com', 'War-Art-Through-Creative-Battles', 'dp', '1936891026']

>>> domain, *rest, asin = url.split('/')[2:-1]
>>> domain
'www.amazon.com'
>>> rest
['War-Art-Through-Creative-Battles', 'dp']
>>> asin
'1936891026'

# this works too of course
>>> elements = url.split('/')
>>> elements[2]
'www.amazon.com'
>>> elements[-2]
'1936891026'