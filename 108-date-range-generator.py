>>> from pprint import pprint as pp
>>> from datetime import date, timedelta

>>> def get_week_dates(start_date, num_weeks=10):
...     if start_date.weekday() != 0:
...         raise ValueError("Start date needs to be a Monday")
...
...     for i in range(num_weeks):
...         start = start_date + timedelta(days=i*7)
...         end = start + timedelta(days=6)
...         yield start, end
...
# oops it's Wed now
>>> pp(list(get_week_dates(date.today())))
...
ValueError: Start date needs to be a Monday

# so let's go 2 days back
>>> mon = date.today() - timedelta(days=2)
>>> pp(list(get_week_dates(mon)))
[(datetime.date(2020, 11, 16), datetime.date(2020, 11, 22)),
 (datetime.date(2020, 11, 23), datetime.date(2020, 11, 29)),
...