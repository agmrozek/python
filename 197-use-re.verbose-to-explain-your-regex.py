>>> import re
>>> bio = """
... name: PyBites
... origin: Worldwide
... born: 2016-12-19
... """
>>> pat = re.compile(r"""
...      \nname:\s         # a newline, then a literal string and a space
...      (?P<name>.*)\n    # capture name, then a newline
...      origin:\s         # literal string followed by a space
...      (?P<origin>.*)\n  # capture origin, then a newline
...      born:\s           # literal string followed by a space
...      (?P<born>.*)\n    # capture born date, then a newline
... """, re.VERBOSE)
>>>
>>> m = pat.match(bio)
>>> m
<re.Match object; span=(0, 50), match='\nname: PyBites\norigin: Worldwide\nborn: 2016-12>
>>> m.groupdict()
{'name': 'PyBites', 'origin': 'Worldwide', 'born': '2016-12-19'}
>>> m.group('name'), m.group('origin'), m.group('born')
('PyBites', 'Worldwide', '2016-12-19')