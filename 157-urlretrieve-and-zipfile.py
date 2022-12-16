>>> from os import listdir
>>> from zipfile import ZipFile
>>> from urllib.request import urlretrieve

>>> data_zip = "temp.zip"
>>> urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/311-data.zip", data_zip)
('temp.zip', <http.client.HTTPMessage object at 0x7f87d55c43d0>)

>>> ZipFile(data_zip).extractall("/tmp/temp")

>>> listdir('/tmp/temp')
['tf_idf.py', 'tf-idf.csv', 'samples.pkl', 'samples.txt', 'stop_words.py']