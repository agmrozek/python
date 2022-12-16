>>> from datetime import datetime, timedelta

>>> class Promo:
...     def __init__(self, name, expires=None):
...         self.name = name
...         self.expires = expires or datetime.now()
...     @property
...     def expired(self):
...         return datetime.now() > self.expires
...

>>> promo = Promo('Halloween', expires=datetime.now() + timedelta(seconds=5))
>>> promo.expired
False
# wait 5 seconds
>>> promo.expired
True