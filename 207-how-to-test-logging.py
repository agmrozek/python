# script.py
import logging

def func():
    logging.debug("a debug message to ignore")
    logging.info("an info message")
    try:
        1 / 0
    except ZeroDivisionError:
        logging.exception("cannot divide by 0")

# test_script.py
import logging

from script import func

def test_func(caplog):
    caplog.set_level(logging.INFO)
    func()
    record1, record2 = caplog.records
    assert record1.levelname == "INFO"  # no debug
    assert record1.message == "an info message"
    assert record2.message == "cannot divide by 0"
    assert record2.exc_info[0] is ZeroDivisionError