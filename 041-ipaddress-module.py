>>> import ipaddress
>>> ipaddress.ip_address('192.168.0.1')
IPv4Address('192.168.0.1')

>>> my_ip = ipaddress.ip_address('fe80:0:0:0:200:f8ff:fe21:67cf')
>>> my_ip
IPv6Address('fe80::200:f8ff:fe21:67cf')
>>> my_ip.version
6

>>> net4 = ipaddress.ip_network('192.0.2.0/24')
>>> net4.netmask
IPv4Address('255.255.255.0')
>>> net4.num_addresses
256
>>> for x in net4.hosts():
...     print(x)  
192.0.2.1
...
192.0.2.254