$ more script.py
def sum_numbers(*numbers):
    return sum(numbers)

$ more test.py
from script import sum_numbers

def test_sum_numbers_ints():
    assert sum_numbers(1, 2, 3) == 6

def test_sum_numbers_floats():
    assert sum_numbers(0.1, 0.2) == 0.3  # uh-oh

$ pytest test.py
...
E       assert 0.30000000000000004 == 0.3
E        +  where 0.30000000000000004 = sum_numbers(0.1, 0.2)
...
1 failed, 1 passed in 0.06s

$ more test.py
from pytest import approx
...
def test_sum_numbers_floats():
    assert sum_numbers(0.1, 0.2) == approx(0.3)  # this passes