import datetime

from freezegun import freeze_time

from tomorrow import tomorrow


@freeze_time('2020-07-09')
def test_no_args():
    assert tomorrow() == datetime.date(2020, 7, 10)