>>> import hashlib
>>> email = 'bob@pybit.es'
>>> hashlib.md5(email)
...
TypeError: Unicode-objects must be encoded before hashing
>>> hashlib.md5(email.encode('utf-8'))
<md5 _hashlib.HASH object @ 0x7fddf88e75f0>
>>> dir(hashlib.md5(email.encode('utf-8')))
[..., 'block_size', 'copy', 'digest', 'digest_size', 'hexdigest', 'name', 'update']
>>> hashlib.md5(email.encode('utf-8')).digest()
b"[\x135mFz\xf8\x861P<'\xa3\xd0\xe0\xcf"
>>> hashlib.md5(email.encode('utf-8')).hexdigest()
'5b13356d467af88631503c27a3d0e0cf'