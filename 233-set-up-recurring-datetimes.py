>>> from dateutil.rrule import rrule, WEEKLY, SU, TU, TH
>>> from dateutil.parser import parse
>>> from pprint import pprint as pp
>>> dates = rrule(WEEKLY, count=10, wkst=SU, byweekday=(TU,TH),
...               dtstart=parse("20210118T160000"))
>>> pp(list(dates))
[datetime.datetime(2021, 1, 19, 16, 0),
 datetime.datetime(2021, 1, 21, 16, 0),
 datetime.datetime(2021, 1, 26, 16, 0),
 datetime.datetime(2021, 1, 28, 16, 0),
 datetime.datetime(2021, 2, 2, 16, 0),
 datetime.datetime(2021, 2, 4, 16, 0),
 datetime.datetime(2021, 2, 9, 16, 0),
 datetime.datetime(2021, 2, 11, 16, 0),
 datetime.datetime(2021, 2, 16, 16, 0),
 datetime.datetime(2021, 2, 18, 16, 0)]