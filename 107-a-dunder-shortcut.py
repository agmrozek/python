from functools import total_ordering

@total_ordering
class Account:
    ...
    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

>>> acc = Account()
>>> acc2 = Account()
... account activity ...

# all comparison operators work
>>> acc2 > acc
True

>>> acc2 < acc
False

>>> acc == acc2
False