>>> import bs4
>>> import requests

>>> url = ("https://email-verify.my-addr.com/list-of-most-"
...        "popular-email-domains.php")
>>> resp = requests.get(url)
>>> soup = bs4.BeautifulSoup(resp.content, 'html.parser')

>>> div = soup.find("div", attrs={"class": "middle_info_noborder"})
>>> trs = div.find_all('tr')

>>> for tr in trs[:5]:
...     tr.find_all('td')[2:]
...
[<td>gmail.com</td>, <td>17.74% </td>]
[<td>yahoo.com</td>, <td>17.34% </td>]
[<td>hotmail.com</td>, <td>15.53% </td>]
[<td>aol.com</td>, <td>3.2% </td>]
[<td>hotmail.co.uk</td>, <td>1.27% </td>]

>>> tr1 = trs[0]
>>> tr1.find_all('td')[2:]
[<td>gmail.com</td>, <td>17.74% </td>]
>>> [t.text.strip() for t in tr1.find_all('td')[2:]]
['gmail.com', '17.74%']