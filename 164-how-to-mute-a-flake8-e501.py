# 1. ignore one off violations in-line
MSG = """
Hey {name},
...
<a href="{link}" target="_blank"><img src="{img}" alt="{title}" style="width: 100%;"></a>
...
...
"""  # noqa E501

# 2. ignore from the command line
flake8 --ignore=E501 path/to/files/

# 3. ignore per project (~/.config/flake8 = global, be careful!)
(project_folder) $ more .flake8
[flake8]
ignore = E501