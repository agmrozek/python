>>> import re
>>> html = ("<div><p>Today a quick article on a nice caching module"
...         " when working with APIs.</p><p>Read more ...</p></div>")
>>> m = re.search('<p>.*</p>', html)
>>> m
<re.Match object; span=(5, 102), match='<p>Today a quick article on a nice caching module>

# oops, matched both paragraphs
>>> m.group()
'<p>Today a quick article on a nice caching module when working with APIs.</p><p>Read more ...</p>'

# adding a ? after the pattern to only match up until the first closing paragraph tag
>>> m = re.search('<p>.*?</p>', html)
>>> m
# span matches 20 chars less
<re.Match object; span=(5, 82), match='<p>Today a quick article on a nice caching module>

# again, group is great to refer to the matching substring
>>> m.group()
'<p>Today a quick article on a nice caching module when working with APIs.</p>'