>>> vowels = 'aeiou'
>>> text = "It's Friday evening, which means X-FILES night"
>>> table = {c: c.swapcase() for c in vowels + vowels.upper()}
>>> table
{'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U', 'A': 'a', 'E': 'e',
 'I': 'i', 'O': 'o', 'U': 'u'}

>>> translation = text.maketrans(table)
# keys are outputs of ord() = integer representation of (Unicode) characters
# so ord('A') -> 65, ord('E') -> 69, etc.
>>> translation
{97: 'A', 101: 'E', 105: 'I', 111: 'O', 117: 'U', 65: 'a', 69: 'e',
 73: 'i', 79: 'o', 85: 'u'}

# apply the translation mapping, effectively "swapcasing" all vowels
>>> text.translate(translation)
"it's FrIdAy EvEnIng, whIch mEAns X-FiLeS nIght"

# an alternative: using join + a generator expression
>>> "".join(table.get(c, c) for c in text)
"it's FrIdAy EvEnIng, whIch mEAns X-FiLeS nIght"