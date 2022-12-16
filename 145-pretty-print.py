>>> from collections import Counter
>>> import pprint
>>> from itertools import chain

# from a previous tip
>>> articles = [a.text for a in soup.find_all('a', href=True)
...             if 'https://pybit.es' in a['href']]
# get all words from articles
>>> words = chain(*[art.split() for art in articles])
# get the most common words
>>> most_common = Counter(words).most_common(20)

# print them nicely
>>> pp = pprint.PrettyPrinter(width=40, compact=True)
>>> pp.pprint(most_common)
[('-', 214), ('Code', 141),
 ('Challenge', 122), ('Twitter', 101),
 ('to', 73), ('Python', 70), ('a', 67),
 ('Digest', 60), ('Review', 54),
 ('2017', 52), ('and', 45),
 ('PyBites', 43), ('2018', 39),
 ('of', 37), ('Week', 36),
 ('digest', 36), ('week', 35),
 ('How', 32), ('With', 29),
 ('the', 28)]