>>> from datetime import datetime
>>> import time
>>> import sched
>>> s = sched.scheduler(time.time, time.sleep)
>>> def hydrate(sc):
...     print(datetime.now(), "Sip water!")
...     s.enter(300, 1, hydrate, (sc,))
...
>>> s.enter(300, 1, hydrate, (s,))
Event(time=1611405298.4987588, priority=1, action=...
>>> s.run()
2021-01-23 13:34:58.499065 Sip water!
2021-01-23 13:39:58.500204 Sip water!
...
# a nicer way:
>>> import schedule  # PyPI package
>>> def hydrate():
...     print(datetime.now(), "Sip water!")
...
>>> schedule.every(5).minutes.do(hydrate)
Every 5 minutes do hydrate() (... next run: 2021-01-23 14:39:29)
>>> while True:
...     schedule.run_pending()
...     time.sleep(1)
...
2021-01-23 14:39:30.087519 Sip water!
2021-01-23 14:44:30.714231 Sip water!
...