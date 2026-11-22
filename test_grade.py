def get_status(student):
    if "marks" not in student:
        return "No Data"
    elif student["marks"] >= 40:
        return "Pass"
    else:
        return "Fail"


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