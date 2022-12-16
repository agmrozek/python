>>> import argparse
>>> parser = argparse.ArgumentParser(description='Calculate your BMI.')
>>> parser.add_argument("-w", "--weight", type=int, help='Your weight in kg')
_StoreAction(option_strings=['-w', '--weight'], ...
>>> parser.add_argument("-l", "--length", type=int, help='Your length in cm')
_StoreAction(option_strings=['-l', '--length'], ...
>>> parser.parse_args(["-w", '80', "--length", '186'])
Namespace(weight=80, length=186)

# cannot take other args:
>>> try:
...     parser.parse_args(["-w", '80', "--length", '186', "--years", "23"])
... except SystemExit:  # prevent REPL exit
...     pass
...
usage: [-h] [-w WEIGHT] [-l LENGTH]
: error: unrecognized arguments: --years 23

# this way we can:
>>> known, unknown = parser.parse_known_args(["-w", '80', "--length", '186', "--years", "23"])
>>> known
Namespace(weight=80, length=186)
>>> unknown
['--years', '23']