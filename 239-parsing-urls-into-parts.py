>>> from urllib.parse import urlparse, urlunparse, ParseResult
>>> url = "https://tim.blog/2019/03/21/learn-to-code/"

>>> parts = urlparse(url)
>>> parts
ParseResult(scheme='https', netloc='tim.blog',
            path='/2019/03/21/learn-to-code/', params='', query='', 
            fragment='')
>>> parts[1]
'tim.blog'
>>> parts.netloc
'tim.blog'

# converting parts into URL and manipulating it:
>>> urlunparse(parts)
'https://tim.blog/2019/03/21/learn-to-code/'
>>> parts.netloc = "pybit.es"
...
AttributeError: can't set attribute
>>> urlunparse(parts._replace(netloc='fourhourworkweek.com', query='share=twitter'))
'https://fourhourworkweek.com/2019/03/21/learn-to-code/?share=twitter'