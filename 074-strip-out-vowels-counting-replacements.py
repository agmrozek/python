>>> import re
>>> vowels = 'aeiou'
>>> text = """
... The Zen of Python, by Tim Peters
...
... Beautiful is better than ugly.
... [truncated]
... """
>>> new_string, number_of_subs_made = re.subn(f'[{vowels}]', '*', text, flags=re.I)
>>> new_string[:10]
'\nTh* Z*n *'
>>> number_of_subs_made
262