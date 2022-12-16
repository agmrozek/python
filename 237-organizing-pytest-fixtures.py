# https://github.com/PyBites-Open-Source/pysource
# conftest.py
...
...
SOURCE_CODE = dict(
    choice=choice, match=match,
    getsource=getsource,
    this=this, capwords=capwords
)

@pytest.fixture(scope='module')
def source_code():
    return SOURCE_CODE

# this fixture can now be used in another test modules
# test_pysource.py 
...
@pytest.mark.parametrize("func", [
    choice, match, ...
])
def test_print_source(func, capfd, source_code):
    print_source(func)
    ...
    assert actual == expected