(venv) $ pip install django-extensions ipython

# settings/local.py
INSTALLED_APPS = INSTALLED_APPS + [
    'django_extensions',
]

(venv) $ python manage.py shell_plus --ipython
# Shell Plus Model Imports
from books.models import Badge, Book, BookNote, Search, UserBook
from django.contrib.admin.models import LogEntry
...
from goal.models import Goal
from pomodoro.models import Pomodoro
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
...
In [1]: Book  # already imported
Out[1]: books.models.Book
In [2]: Book.objects.count()
Out[2]: 2
In [3]: Book.objects.last()
Out[3]: <Book: 2 1ZxxDwAAQBAJ Think & Grow Rich>