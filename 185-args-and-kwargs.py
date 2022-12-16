>>> def send_email(from_, to='me', *cc, **messages):
...     print(f"{from_=} / {to=} / {cc=} / {messages=}")
...
# need at least from_ (using an underscore to not clash with a keyword)
>>> send_email()
...
TypeError: send_email() missing 1 required positional argument: 'from_'
# called with 1 arg, to defaults to 'me'
>>> send_email('info@pybit.es')
from_='info@pybit.es' / to='me' / cc=() / messages={}
# using *args
>>> send_email('info@pybit.es', '1@example.com', '2@example.com', '3@example.com')
from_='info@pybit.es' / to='1@example.com' / cc=('2@example.com', '3@example.com') / messages={}
# using *args and **kwargs
>>> send_email('info@pybit.es', '1@example.com', '2@example.com', intro='hello', body='content', outro='kind regards')
from_='info@pybit.es' / to='1@example.com' / cc=('2@example.com',) / messages={'intro': 'hello', 'body': 'content', 'outro': 'kind regards'}
# using * and ** unpacking
>>> cc = ('1@example.com', '2@example.com', '3@example.com')
>>> messages = {'intro': 'hello', 'body': 'content', 'outro': 'kind regards'}
>>> send_email('info@pybit.es', 'another@email.com', *cc, **messages)
from_='info@pybit.es' / to='another@email.com' / cc=('1@example.com', '2@example.com', '3@example.com') / messages={'intro': 'hello', 'body': 'content', 'outro': 'kind regards'}