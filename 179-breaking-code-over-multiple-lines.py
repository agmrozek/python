# break function args and dict (key, value) pairs
return render(request,
              'pomodoro/pomodoro.html',
              {'key': value, ...})

# break up ORM queries
completed_books_this_year = UserBook.objects.filter(
    user=user, status=COMPLETED, completed__year=goal.year
)

# multiline string
assert ('<input class="js-favorite" title="favorite"'
        f' type="checkbox" bookid={snippet}') in html

# set compehensions
ids = {re.sub(r'.*id=', '', link.attrs['href'])
       for link in links
       if "/store/books/details/" in link.attrs['href']}

# function / generator expression
return sum(
    int(book.book.pages) if str(book.book.pages).isdigit() else 0
    for book in books if book.done_reading)

# break up conditionals
return (path in no_sidebar_pages
        or path.startswith('/tips/'))