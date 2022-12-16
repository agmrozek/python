>>> import csv

$ cat names-with-header.csv
id,first_name,last_name
1,Bibbye,Wield
2,Hewett,Yushachkov
3,Jory,Broune

$ cat names-without-header.csv
1,Pavia,Soro
2,Marna,Gwatkin
3,Melanie,Gribble

>>> def csv_has_header(file):
...     with open(file, 'r') as csvfile:
...         sniffer = csv.Sniffer()
...         return sniffer.has_header(csvfile.read(2048))
...

>>> csv_has_header('names-with-header.csv')
True
>>> csv_has_header('names-without-header.csv')
False