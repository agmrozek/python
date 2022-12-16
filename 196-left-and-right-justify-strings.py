>>> import random
>>> names = 'Julian Bob Martin Rodolfo'.split()
>>> scores = random.sample(range(1, 11), len(names))
>>> scores
[8, 3, 9, 2]
>>> for name, score in zip(names, scores):
...     print(f"{name:<20} {score}")
...
Julian               8
Bob                  3
Martin               9
Rodolfo              2
>>> for name, score in zip(names, scores):
...     print(f"{name:^20} | {score:<5}")
...
       Julian        | 8
        Bob          | 3
       Martin        | 9
      Rodolfo        | 2
>>> for name, score in zip(names, scores):
...     print(f"{name:>20} | {score:<05}")
...
              Julian | 80000
                 Bob | 30000
              Martin | 90000
             Rodolfo | 20000