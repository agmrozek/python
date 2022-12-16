# script.py
from time import sleep

def call_api():
    sleep(60)  # faking a timeout
    return dict(
        status=200,
        response=[1, 2, 3])

# test_script.py
from script import call_api

def test_call_api():
    resp = call_api()
    assert resp['status'] == 200
    assert resp['response'] == [1, 2, 3]

$ pytest test_script.py --timeout=3
# output truncated
plugins: timeout-1.4.2
...
== FAILURES ==
__ test_call_api __
...
    def call_api():
>       sleep(60)  # faking a timeout
E       Failed: Timeout >3.0s
...
== 1 failed in 3.05s ==