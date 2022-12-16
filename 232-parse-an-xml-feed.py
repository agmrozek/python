>>> from collections import Counter
>>> import xml.etree.ElementTree as ET
>>> import requests
>>> pybites_rss_feed = "https://pybit.es/feeds/all.rss.xml"
>>> resp = requests.get(pybites_rss_feed)
>>> tree = ET.fromstring(resp.content)
>>> categories = (e.text for e in tree.findall("./channel/item/category"))
>>> most_comon_categories = Counter(categories).most_common(10)
>>> print(*most_comon_categories, sep='\n')
('learning', 102)
('news', 98)
('twitter', 96)
('python', 88)
('tips', 74)
('codechallenges', 72)
('Flask', 68)
('pybites', 67)
('Django', 54)
('data science', 38)