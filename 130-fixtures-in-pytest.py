# module to test (full code linked below)
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __str__(self):
        return f"Car: {self.model} ({self.year})"
     ...
# test module
import pytest
from cars import Car

# by default fixtures use "function" scope = they run for each test function (use "module" / "session" scope to persist across tests)

@pytest.fixture
def car():
    return Car("Sierra", 2020)

def test_str(car):  # fixtures are passed in as test function arguments
    assert str(car) == 'Car: Sierra (2020)'