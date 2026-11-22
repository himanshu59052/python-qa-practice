from grade import get_status
import pytest

def test_pass():
    assert get_status({"naam": "Himanshu", "marks": 55}) == "Pass"


def test_boundary_40():
    assert get_status({"naam": "Ravi", "marks": 40}) == "Pass"

def test_no_data():
    assert get_status({"naam": "Amit"})=="No Data"

def test_less_marks():
    assert get_status({"naam": "Himanshu", "marks": 30}) == "Fail"


def test_l39_marks():
    assert get_status({"naam": "Himanshu", "marks": 39}) == "Fail"

@pytest.mark.parametrize("marks, expected",[
   (90, "Pass"),
    (55, "Pass"),
    (40, "Pass"),
    (39, "Fail"),
    (30, "Fail"),
    (0, "Fail"),
])
def test_marks(marks, expected):
    assert get_status({"naam": "Test", "marks": marks}) ==expected