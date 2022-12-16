>>> names = ['Phyllis', 'Amelina', 'Delaney', 'Kinsley', 'Carena',
...          'Imogene', 'Tyler', 'Olag', 'Gilberta', 'Rufe']
>>>
>>> def print_names_to_columns(names: list[str], cols: int = 2) -> None:
...     for i, name in enumerate(names, 1):  # you can start at 1!
...         print(f"| {name:<10}", end="")
...         if i % cols == 0 or i == len(names):
...             print()
...
>>> print_names_to_columns(names)
| Phyllis   | Amelina
| Delaney   | Kinsley
| Carena    | Imogene
| Tyler     | Olag
| Gilberta  | Rufe
>>> print_names_to_columns(names, 4)
| Phyllis   | Amelina   | Delaney   | Kinsley
| Carena    | Imogene   | Tyler     | Olag
| Gilberta  | Rufe