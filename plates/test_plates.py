from plates import is_valid


def test_is_valid():
    assert is_valid("AAA222") == True
    assert is_valid("BBB222") == True
