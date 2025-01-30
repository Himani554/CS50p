from seasons import correctDate
from seasons import writeInWords
import pytest

def test_Date():
    with pytest.raises(SystemExit):
        correctDate("5 january,1945")
    with pytest.raises(SystemExit):
        correctDate("January 1, 1999")



    with pytest.raises(SystemExit):
        correctDate("1999.01.01")


    with pytest.raises(SystemExit):
        correctDate("cat")


