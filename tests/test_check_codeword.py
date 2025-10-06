from lib.check_codeword import *

def test_check_invalid_input():
    assert check_codeword(" ") == "WRONG!"
    assert check_codeword("123a") == "WRONG!"

def test_check_horse_input():
    assert check_codeword("horse") == "Correct! Come in."

def test_check_startswith_h_and_endswith_e():
    assert check_codeword("hose") == "Close, but nope."