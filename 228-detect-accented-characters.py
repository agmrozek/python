>>> from unicodedata import decomposition
>>> for c in 'Cataluña':
...     c, decomposition(c)
...
('C', '')  # = no character decomposition mapping
('a', '')
('t', '')
('a', '')
('l', '')
('u', '')
('ñ', '006E 0303')  # bingo, this is an accented letter
('a', '')
>>> text = ("La capital de Cataluña, es la ciudad más visitada "
...         "de España y la segunda más poblada.")
# use enumerate to get the indices or positions of the matches
>>> positions = [i for i, c in enumerate(text) if decomposition(c)]
>>> for pos in positions:
...     pos, text[pos]
...
(20, 'ñ')
(38, 'á')
(57, 'ñ')
(74, 'á')