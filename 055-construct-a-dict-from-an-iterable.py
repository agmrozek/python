>>> nodes
['abcd:22', 'efgh:80', 'ijkl:443']
>>> dict(node.split(':') for node in nodes)
{'abcd': '22', 'efgh': '80', 'ijkl': '443'}

>>> nodes.append('mno:555:bug')
>>> nodes
['abcd:22', 'efgh:80', 'ijkl:443', 'mno:555:bug']

# oops
>>> dict(node.split(':') for node in nodes)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: dictionary update sequence element #3 has length 3; 2 is required

# split has our back though
>>> dict(node.split(':', 1) for node in nodes)
{'abcd': '22', 'efgh': '80', 'ijkl': '443', 'mno': '555:bug'}