def greeting(name=None):
    """
    >>> greeting()
    'Hello Stranger!'
    >>> greeting('bob')
    'Hello Bob!'
    """
    name = "Stranger" if name is None else name
    return f"Hello {name.title()}!"

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# no output on a passing test, removing the exclamation point in the expected output produces:
$ python script.py
**********************************************************************
File "script.py", line 5, in __main__.greeting
Failed example:
    greeting('bob')
Expected:
    'Hello Bob'
Got:
    'Hello Bob!'
**********************************************************************
1 items had failures:
   1 of   2 in __main__.greeting
***Test Failed*** 1 failures.