>>> import os, argparse
>>> from collections import ChainMap
>>> defaults = {'color': 'red'}

>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('-c', '--color')
>>> args = parser.parse_args()

>>> cli_args = {k: v for k, v in vars(args).items() if v}
>>> combined = ChainMap(cli_args, os.environ, defaults)
>>> combined['color']
red  # default

>>> os.environ['color'] = 'blue'
>>> combined = ChainMap(cli_args, os.environ, defaults)
>>> combined['color']
blue  # env variable takes precedence

>>> args.color = 'green'  # as if given from the command line
>>> cli_args = {k: v for k, v in vars(args).items() if v}
>>> combined = ChainMap(cli_args, os.environ, defaults)
>>> combined['color']
green  # command line variable takes precedence