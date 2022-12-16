>>> import calendar

>>> print(calendar.month(2020, 10))
    October 2020
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

>>> help(calendar.month)
...
formatmonth(theyear, themonth, w=0, l=0) method of calendar.TextCalendar instance
    Return a month's calendar string (multi-line).

# make the columns wider
>>> print(calendar.month(2020, 10, w=5))
               October 2020
 Mon   Tue   Wed   Thu   Fri   Sat   Sun
                     1     2     3     4
   5     6     7     8     9    10    11
  12    13    14    15    16    17    18
  19    20    21    22    23    24    25
  26    27    28    29    30    31