>>> s = ("It's almost 3 years we launched our PyBites platform"
...      ", which now hosts 300+ exercises, up to the next 100 Bites")
>>>
>>> [int(word) for word in s.split() if word.isdigit()]
[3, 100]