>>> numbers = list(range(1, 11))
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numbers2 = [num*10 for num in numbers]
>>> numbers2
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# define and reuse:
>>> first_N = slice(0, 2)
>>> numbers[first_N]
[1, 2]
>>> numbers2[first_N]
[10, 20]

# wait, I wanted the first three, no problem, update once:
>>> first_N = slice(0, 3)
>>> numbers[first_N]
[1, 2, 3]
>>> numbers2[first_N]
[10, 20, 30]

# use None to go till the end
>>> last_three = slice(-3, 0)
>>> numbers[last_three]
[]
>>> last_three = slice(-3, None)
>>> numbers[last_three]
[8, 9, 10]