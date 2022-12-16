>>> from datetime import date
>>> date.today()
datetime.date(2021, 1, 11)
>>> date.today().timetuple()
time.struct_time(tm_year=2021, tm_mon=1, tm_mday=11, tm_hour=0,
                 tm_min=0, tm_sec=0, tm_wday=0, tm_yday=11,
                 tm_isdst=-1)
>>> date.today().timetuple().tm_yday
11
>>> day_in_july = date(2021, 7, 14)
>>> day_in_july.timetuple()
time.struct_time(tm_year=2021, tm_mon=7, tm_mday=14, tm_hour=0,
                 tm_min=0, tm_sec=0, tm_wday=2, tm_yday=195,
                 tm_isdst=-1)
>>> day_in_july.timetuple().tm_yday
195
# another way:
>>> int(day_in_july.strftime('%j'))
195