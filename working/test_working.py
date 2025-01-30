import pytest
from working import convert

def test_convert_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_convert_2():
    assert convert("9 AM to 5 PM") != "05:00 to 17:00"
    assert convert("10:30 PM to 8 AM") != "22:36 to 08:00"

def test_convert_3():
    with pytest.raises(ValueError):
        convert("15 AM to 4 PM")
    with pytest.raises(ValueError):
        convert("17:56 AM to 42:45 PM")
    with pytest.raises(ValueError):
        convert("5:45 AM - 4:56 PM")




