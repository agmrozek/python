>>> import re
>>> s = "@P and @PyBites should both work :)"

# oops!
>>> s.replace("@P", "<a href='#P'>{at_name}</a>")
"<a href='#P'>{at_name}</a> and <a href='#P'>{at_name}</a>yBites should both work :)"

# match right word boundary
>>> s = re.sub(r"@P\b", "<a href='#P'>@P</a>", s)

# good: only @P not replaced
>>> s
"<a href='#P'>@P</a> and @PyBites should both work :)"

# yes, you could do this with one re.sub (\w+), but here we are matching
# exact usernames, one by one
>>> s = re.sub(r"@PyBites\b", "<a href='#PyBites'>@PyBites</a>", s)

# all good
>>> s
"<a href='#P'>@P</a> and <a href='#PyBites'>@PyBites</a> should both work :)"