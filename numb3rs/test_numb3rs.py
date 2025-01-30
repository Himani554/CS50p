from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1") == False
    assert validate("1.2") == False
    assert validate("1.2.3") == False


def test_range_validate():
    assert validate("1.1.1.500") == False
    assert validate("cat") == False
    assert validate("1.2.cat.3") == False
    assert validate("500.1.1.1") == False
    assert validate("1.1.500.1") == False
    assert validate("1.500.1.1") == False

