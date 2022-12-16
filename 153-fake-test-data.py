# pip install Django && python manage.py shell
In [1]: from django.contrib.auth.models import User
In [2]: from faker import Faker
In [3]: fake = Faker()
# create some fake data
In [4]: first_name, last_name, domain = fake.first_name(), fake.last_name(), fake.safe_domain_name()
In [5]: first_name, last_name, domain
Out[5]: ('Douglas', 'Tapia', 'example.net')
In [6]: username = f"{first_name.lower()}.{last_name.lower()}"
In [7]: email = f"{username}@{domain}"
# create a Django User object
In [8]: u = User(first_name=first_name, last_name=last_name, email=email, username=username)
In [9]: u
Out[9]: <User: douglas.tapia>
In [10]: vars(u)
Out[10]:
{'_state': <django.db.models.base.ModelState at 0x7fef04fe23d0>,
 'id': None,
…
 'username': 'douglas.tapia',
 'first_name': 'Douglas',
 'last_name': 'Tapia',
 'email': 'douglas.tapia@example.net',
 …
 'date_joined': datetime.datetime(2020, 11, 25, 7, 38, 44, 52703, tzinfo=<UTC>)}