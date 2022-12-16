>>> from datetime import date
>>> help(date.today().weekday)

Help on built-in function weekday:

weekday(...) method of datetime.date instance
    Return the day of the week represented by the date.
    Monday == 0 ... Sunday == 6


# using it for a Django command for example

from django.core.management.base import BaseCommand

IS_MONDAY = date.today().weekday() == 0


class Command(BaseCommand):

    def handle(self, *args, **options):
        # logic for every day

        if IS_MONDAY:
            # additional logic only to be run on Monday ...