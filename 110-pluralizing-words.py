>>> for num_games in (0, 1, 2, 10):
...     num_games, f"game{'' if num_games == 1 else 's'}"
...
(0, 'games')
(1, 'game')
(2, 'games')
(10, 'games')

>>> from gettext import ngettext
>>> for num_games in (0, 1, 2, 10):
...     num_games, ngettext("game", "games", num_games)
...
(0, 'games')
(1, 'game')
(2, 'games')
(10, 'games')