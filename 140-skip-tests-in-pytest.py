# comments.py (code with a syntax error)
def time_printer():
    this line should be commented

# test_comments.py
import pytest

def _can_import():
    try:
        import comments  # noqa F401
        return True
    except IndentationError:
        return False

def test_import_fails_because_not_all_garbage_commented():
    if not _can_import():
        raise pytest.fail(…

@pytest.mark.skipif(not _can_import(), reason="Only run if import works")
def test_output_time_printer_with_time_arg_returns_string(capfd):
    # tests past successful import ...

# nicer output + skip other test
$ pytest [output truncated]
E           Failed: comments.py raised an IndentationError, did you comment it properly?
=== 1 failed, 1 skipped in 0.05 seconds ===