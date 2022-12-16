>>> s = "Here's food for thought, let's say title casing isn't easy ..."

# oops
>>> s.title()
"Here'S Food For Thought, Let'S Say Title Casing Isn'T Easy ..."

>>> import string
>>> string.capwords(s)
"Here's Food For Thought, Let's Say Title Casing Isn't Easy ..."

# similar to:
>>> s.split()
["Here's", 'food', 'for', 'thought,', "let's", 'say', 'title', 'casing', "isn't", 'easy', '...']
>>> [w.capitalize() for w in s.split()]
["Here's", 'Food', 'For', 'Thought,', "Let's", 'Say', 'Title', 'Casing', "Isn't", 'Easy', '...']
>>> ' '.join(w.capitalize() for w in s.split())
"Here's Food For Thought, Let's Say Title Casing Isn't Easy ..."
>>> ' '.join(w.capitalize() for w in s.split()) == string.capwords(s)
True

# use a different string to split on:
>>> string.capwords(s, sep="'")
"Here'S food for thought, let'S say title casing isn'T easy ..."