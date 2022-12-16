# no __str__ method
class Book(models.Model):
    bookid = models.CharField(max_length=20)  # google bookid
    title = models.CharField(max_length=200)
    ...

$ python manage.py shell
>>> from books.models import Book
>>> Book.objects.count()
2
>>> Book.objects.last()
<Book: Book object (2)>

# with __str__ method
class Book(models.Model):
    bookid = models.CharField(max_length=20)  # google bookid
    title = models.CharField(max_length=200)
    ...
    
    def __str__(self):
        return f'{self.id} {self.bookid} {self.title}'

$ python manage.py shell
>>> from books.models import Book
>>> Book.objects.last()
<Book: 2 1ZxxDwAAQBAJ Think & Grow Rich>
>>> Book.objects.first()
<Book: 1 1KuwDwAAQBAJ The Coaching Habit>