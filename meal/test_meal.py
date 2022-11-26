from meal import convert
def test_convert():
    assert convert("7:30") == 7.5
    assert convert("8:30") == 8.5
