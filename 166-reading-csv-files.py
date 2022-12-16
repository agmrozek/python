$ cat names.csv
id,first_name,last_name
1,Bibbye,Wield
2,Hewett,Yushachkov
3,Jory,Broune

>>> import csv
>>> with open('names.csv') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...         print(row)
...
{'id': '1', 'first_name': 'Bibbye', 'last_name': 'Wield'}
{'id': '2', 'first_name': 'Hewett', 'last_name': 'Yushachkov'}
{'id': '3', 'first_name': 'Jory', 'last_name': 'Broune'}