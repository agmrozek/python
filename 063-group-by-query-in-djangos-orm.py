>>> from django.db.models import Count
>>> from django.contrib.auth.models import User

>>> User.objects.exclude(first_name__exact='').values(
...     'first_name').annotate(
...     name_count=Count('first_name')
... ).order_by('-name_count')[:5].values_list(
...     'first_name', flat=True
... )

<QuerySet ['David', 'Daniel', 'Michael', 'Chris', 'John']>