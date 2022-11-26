

test_isValid():
    assert isValid("1 + 1") == True
    assert isValid("5 - 3") == True
    assert isValid("Test") == False
    assert isValid("5 / 0") == False
