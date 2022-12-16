# script.py
import argparse

parser = argparse.ArgumentParser(description='A simple calculator')
parser.add_argument('-a', '--add', nargs='+', help="Sums numbers")
parser.add_argument('-s', '--sub', nargs='+', help="Subtracts numbers")
parser.add_argument('-m', '--mul', nargs='+', help="Multiplies numbers")
parser.add_argument('-d', '--div', nargs='+', help="Divides numbers")

args = parser.parse_args()

# drop in the debugger
breakpoint()

$ python script.py -a 1 -s 2 -m 3 -d 4

(Pdb) args
(Pdb) vars(args)
{'add': ['1'], 'sub': ['2'], 'mul': ['3'], 'div': ['4']}