from plates import is_valid


def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
