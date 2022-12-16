>>> from dateutil.parser import parse
>>> logs = """
... Wed Apr 10 22:39
... Wed Mar 27 16:24
... Wed Mar 27 15:01
... Sun Mar  3 14:51
... Sun Feb 17 11:36
... Thu Jan 17 21:54
... Mon Jan 14 09:25
... """.strip()

>>> log_lines = reversed(logs.splitlines())
>>> reboots = [parse(line.strip()) for line in log_lines]

>>> uptimes = []
>>> for dt1, dt2 in zip(reboots, reboots[1:]):
...     uptime_days = (dt2 - dt1).days
...     uptimes.append(uptime_days)
...
>>> max(uptimes)
30