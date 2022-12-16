# challenge.py module
from abc import ABC, abstractmethod

class Challenge(ABC):

    def __init__(self, number):
        self.number = number

    @abstractmethod
    def pretty_title(self):
        return 'Subclass should implement'


# test module
import inspect

from challenge import Challenge

def test_baseclass_methods_are_abstract():
    lines = [line.strip() for line in
             inspect.getsourcelines(Challenge)[0]]
    ...
    pretty_title_index = lines.index('def pretty_title(self):')
    assert lines[pretty_title_index - 1] == "@abstractmethod"