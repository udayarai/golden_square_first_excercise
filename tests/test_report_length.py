from lib.report_length import *

def test_with_non_empty_string():
    assert len("Hello") == 5
    assert len("12345") == 5

def test_with_empty_string():
    assert len("") == 0
