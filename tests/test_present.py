import pytest
from lib.present import Present

"""
when we wrap an item 
we get it back when unwrapping
"""

def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33


"""
If we unwrap before wrapping 
we get an error message
"""

def test_unwrap_without_wrapping():
    present = Present()

    with pytest.raises(Exception) as e:
        present.unwrap()
    assert str(e.value) == "No contents have been wrapped."


"""
if we try to wrap twice then an error is raised
"""
def test_wrapping_already_wrapped():
    present = Present()

    present.wrap(33)

    with pytest.raises(Exception) as e:
        present.wrap(44)
    error_message = str(e.value)
    
    assert error_message == "A contents has already been wrapped."

"""
if we try to wrap twice then an error is raised
but the first wrapped value is unchanged
"""
def test_wrapping_already_wrapped_preserves_value():
    present = Present()

    present.wrap(33)
    
    with pytest.raises(Exception) as e:
        present.wrap(44)
    
    assert present.unwrap() == 33