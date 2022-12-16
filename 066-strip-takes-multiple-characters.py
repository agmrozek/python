# real use case on our platform
>>> pytest_summary = "=== 20 passed in 0.05 seconds ===\n"
>>> pytest_summary.strip("= \n")
'20 passed in 0.05 seconds'

# another example from the docs
>>> 'www.example.com'.strip('cmowz.')
'example'
>>> comment_string = '#....... Section 3.2.1 Issue #32 .......'
>>> comment_string.strip('.#! ')
'Section 3.2.1 Issue #32'