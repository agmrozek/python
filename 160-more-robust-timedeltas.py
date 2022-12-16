>>> from datetime import date
>>> pybites_born = date(year=2016, month=12, day=19)
>>> today = date.today()
>>> (today-pybites_born).days
1447

# oops
>>> (today-pybites_born).years  # same for .months
...
AttributeError: 'datetime.timedelta' object has no attribute 'years'

>>> from dateutil.relativedelta import relativedelta, MO
>>> diff = relativedelta(today, pybites_born)
>>> diff.years, diff.months
3, 11

# there are many more options:
>>> today
datetime.date(2020, 12, 5)  # Saturday

>>> today + relativedelta(months=+1, weeks=+1, hour=10)
datetime.datetime(2021, 1, 12, 10, 0)

>>> today + relativedelta(weekday=MO)
datetime.date(2020, 12, 7)