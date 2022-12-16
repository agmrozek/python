>>> from datetime import date
>>> date.today().isocalendar()[1]
30
>>> date(2020, 1, 3).isocalendar()[1]
1
>>> date(2020, 12, 25).isocalendar()[1]
52

# get a range of remaining weeks:
>>> start_week = date.today().isocalendar()[1]
>>> start_week
45
>>> weeks = range(start_week, 53)
>>> list(weeks)
[45, 46, 47, 48, 49, 50, 51, 52]