import pytest
from fuel import convert, gauge

def test_convert_valid_cases():
    assert convert("1/3") == 33
    assert convert("4/5") == 80

def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("dog/cat")
    with pytest.raises(ValueError):
        convert("3/2")

def test_gauge_e():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(-1) == "E"

def test_gauge_f():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(101) == "F"

def test_gauge_percent():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"

if __name__ == "__main__":
    pytest.main()
