>>> import heapq
>>> import random
>>> from operator import itemgetter

>>> numbers = random.sample(range(50), 10)
>>> numbers
[39, 10, 17, 37, 4, 13, 42, 6, 30, 27]
>>> heapq.nlargest(3, numbers)
[42, 39, 37]
>>> heapq.nsmallest(3, numbers)
[4, 6, 10]
>>> heapq.heapify(numbers)
>>> numbers
[4, 6, 13, 30, 10, 17, 42, 37, 39, 27]

>>> n1 = [10, 17, 37, 39]
>>> n2 = [4, 6, 13, 27, 30, 42]
>>> list(heapq.merge(n1, n2))
[4, 6, 10, 13, 17, 27, 30, 37, 39, 42]

>>> user_scores = {'bob': 3, 'julian': 7, 'tim': 10, 'sara': 2}
>>> heapq.nsmallest(2, user_scores)  # by lowest name first char
['bob', 'julian']
>>> heapq.nsmallest(2, user_scores.items(), key=itemgetter(1))  # lowest score
[('sara', 2), ('bob', 3)]
# >>> sorted(user_scores.items(), key=itemgetter(1))[:2]