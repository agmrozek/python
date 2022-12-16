>>> import ipaddress
>>> import socket
>>> ip_addresses = ("192.168.0.2", "127.0.0.1", "192.168.1.257", "1.0x2.3.4",
...                 "2001:0db8:85a3:0000:0000:8a2e:0370:7334")
>>> def valid_ip(ip: str) -> bool:
...     try:
...         ipaddress.ip_address(ip)
...         return True
...     except ValueError:
...         return False
...
>>> def valid_ip4_addr(ip: str) -> bool:
...     try:
...         socket.inet_pton(socket.AF_INET, ip)
...         return True
...     except socket.error:
...         return False
...
>>> for ip in ip_addresses:
...     print(f"{ip:<40} | {str(valid_ip(ip)):<5} | {valid_ip4_addr(ip)}")
...
192.168.0.2                              | True  | True
127.0.0.1                                | True  | True
192.168.1.257                            | False | False
1.0x2.3.4                                | False | False
2001:0db8:85a3:0000:0000:8a2e:0370:7334  | True  | False