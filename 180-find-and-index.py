>>> text = "I want to match premium and premium+ in this sentence"

>>> text.find('premium')
16
>>> text.rfind('premium')
28

>>> text.index('premium')
16
>>> text.rindex('premium')
28

# difference is how they deal with not founds
>>> text.find('nomatch')
-1
>>> text.index('nomatch')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found