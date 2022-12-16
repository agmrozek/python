>>> import bs4
>>> import requests

>>> resp = requests.get('https://pybit.es/archives')
>>> soup = bs4.BeautifulSoup(resp.text, 'html.parser')

>>> matches = [a for a in soup.find_all('a', href=True)
...            if 'beautiful' in a.text.lower()]

>>> for m in matches:
...     print(m.text)
...     print(m['href'])
...
Generating Beautiful Code Snippets with Carbon and Selenium
https://pybit.es/python-tips-carbon-selenium.html
Create a Simple Web Scraper with BeautifulSoup4
https://pybit.es/simplewebscraper.html
Beautiful, idiomatic Python
https://pybit.es/beautiful-python.html