>>> from datetime import datetime
>>> from zoneinfo import ZoneInfo, available_timezones

>>> aus, cet = [tz for tz in available_timezones() if 'Sydney' in tz or 'Madrid' in tz]
>>> aus
'Australia/Sydney'
>>> cet
'Europe/Madrid'

# hours Australia ahead of Spain
>>> def dt(year, month, tz):
...     return datetime(year, month, 1, 0, 0, tzinfo=ZoneInfo(tz))

>>> for month in range(1, 13):
...     delta = dt(2021, month, aus) - dt(2021, month, cet)
...     diff_hours = int(abs(delta.total_seconds()) / 3600)
...     print(f"Month {month} => {diff_hours} hours")
...
Month 1 => 10 hours
Month 2 => 10 hours
Month 3 => 10 hours
Month 4 => 9 hours
Month 5 => 8 hours
Month 6 => 8 hours
...