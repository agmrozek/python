(Pdb) expected
'<a href="/books/nneBa6-mWfgC">Coders at Work</a>'
(Pdb) expected in response.content
*** TypeError: a bytes-like object is required, not 'str'
(Pdb) type(response.content)
<class 'bytes'>
(Pdb) type(response.content.decode())
<class 'str'>
(Pdb) expected in response.content.decode()
True