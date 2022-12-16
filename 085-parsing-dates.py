>>> from datetime import datetime
>>> from dateutil.parser import parse
>>> logline = "INFO 2014-07-03T23:31:22 supybot Killing Driver objects."
>>> date = logline.split()[1]
>>> date
'2014-07-03T23:31:22'
>>> datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
datetime.datetime(2014, 7, 3, 23, 31, 22)
>>> parse(date)
datetime.datetime(2014, 7, 3, 23, 31, 22)