from plates import is_valid

def test_is_valid():
    assert is_valid("abc45") == True
    assert is_valid("0fgf") == False
    assert is_valid("12ggj") == False
    assert is_valid("fj4.5") == False
    assert is_valid("a") == False
    assert is_valid("fgf04") == False
    assert is_valid("g1fh") == False
    assert is_valid("fdhg") == True
    assert is_valid("4563") == False
    assert is_valid("1") == False
    assert is_valid("aaa22a") == False
    assert is_valid("aaa22") == True
