import pytest
from project import Reader,Writer,Data
from unittest.mock import mock_open, patch

def test_Reader():
    assert Reader("231720001")=="Registration No.: 231720001\nName: Himani\nCourse: Data Science\nResults-\n1st Semester: 7\n2nd Semester: 8\n3rd Semester: 6\n4th Semester: 7\n5th Semester: 9\n6th Semester: 8\n7th Semester: None\n8th Semester: None\n"
    assert Reader("345")=="Student not found"


def test_Writer(monkeypatch):
    inputs = ["231760001", "John", "Computer Science", "", "5", "4", "", "5", "7", "7", "5"]

    # Mock input in a single line using monkeypatch.setattr and a lambda
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    # Mock open() in one line and assert file write
    with patch('builtins.open', mock_open()) as mock_file:
        Writer()
        mock_file().write.assert_called()



def test_Data():
    assert Data(456)=="Invalid No."
    assert Data(3)=="Invalid No."


