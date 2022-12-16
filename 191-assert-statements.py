$ more script.py
from datetime import date

pybites_founded = date(2016, 12, 19)

days_alive = (date.today() - pybites_founded).days
years, remainder = divmod(days_alive, 365)

assert remainder == 0, 'Not a PyBites birthday'

print(f"PyBites is {years} years old")

# running this the 17th of Dec, 2 days before our birthday
$ python script.py
Traceback (most recent call last):
...
AssertionError: Not a PyBites birthday

# -O ignored asserts
$ python -O script.py
PyBites is 3 years old