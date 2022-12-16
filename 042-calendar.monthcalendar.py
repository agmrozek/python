>>> import calendar
>>> from datetime import datetime
>>> now = datetime.now()
>>> now
datetime.datetime(2022, 5, 26, 8, 6, 30, 524807)

>>> from pprint import pprint as pp
>>> cal = calendar.monthcalendar(now.year, now.month)
>>> pp(cal)
[[0, 0, 0, 0, 0, 0, 1],
 [2, 3, 4, 5, 6, 7, 8],
 [9, 10, 11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20, 21, 22],
 [23, 24, 25, 26, 27, 28, 29],
 [30, 31, 0, 0, 0, 0, 0]]

>>> cal = calendar.monthcalendar(now.year, now.month+1)
>>> cal[0]
[0, 0, 1, 2, 3, 4, 5]

$ cal 5 2022
      May 2022
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31