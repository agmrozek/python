>>> import feedparser
>>> from operator import itemgetter

>>> blog_feed = feedparser.parse('https://pybit.es/feeds/all.rss.xml')
>>> entry = blog_feed.entries[100]
>>> entry.title
'PyBites Twitter Digest - Issue 27, 2018'
>>> entry.author
'PyBites'
>>> entry.link
'https://pybit.es/twitter_digest_201827.html'
>>> for entry in blog_feed.entries[:5]:
...     itemgetter('link', 'author', 'published')(entry)
...
('https://pybit.es/get-python-source.html', 'Bob', 'Mon, 14 Dec 2020 19:05:00 +0100')
('https://pybit.es/guest-create-aws-lambda-layers.html', 'Michael Aydinbas', 'Mon, 05 Oct 2020 14:22:00 +0200')
('https://pybit.es/guest-clean-text-data.html', 'David Colton', 'Wed, 30 Sep 2020 20:34:00 +0200')
('https://pybit.es/code-reviewing.html', 'Bob', 'Thu, 24 Sep 2020 18:43:00 +0200')
('https://pybit.es/opensource-package-pypi.html', 'Bob', 'Mon, 31 Aug 2020 12:05:00 +0200')