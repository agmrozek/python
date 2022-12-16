>>> from zipfile import ZipFile
>>> my_zip = ZipFile('pybites_bite306.zip')

>>> my_zip.namelist()
['README.md', 'bite.html', 'translate_cds.py', 'test_translate_cds.py', 'git.txt']

>>> readme = my_zip.namelist()[0]
>>> readme
'README.md'

>>> my_zip.read(readme)
b'## [Bite 306. Translate coding sequences to proteins] ...