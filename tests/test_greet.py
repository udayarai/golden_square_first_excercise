from lib.greet import *

def test_greeting_when_name_is_passed():
    result = greet("John")

    assert(result) == "Hello, John!"