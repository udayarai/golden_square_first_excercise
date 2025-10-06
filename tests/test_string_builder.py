from lib.string_builder import StringBuilder

"""
initially return an empty string when nothing is added
"""

def test_initially_returns_empty_string():
    string_builder = StringBuilder()
    assert string_builder.size() == 0
    assert string_builder.output() == ""

"""
adds provided single string 
"""
def test_with_single_added_string():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    assert string_builder.size() == 5
    assert string_builder.output() == "Hello"


"""
adds multiple string
"""
def test_with_multiple_added_string():
    string_builder = StringBuilder()
    string_builder.add("Hello ")
    string_builder.add("John")
    assert string_builder.size() == 10
    assert string_builder.output() == "Hello John"