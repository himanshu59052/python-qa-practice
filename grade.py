def get_status(student):
    if "marks" not in student:
        return "No Data"
    elif student["marks"] >= 40:
        return "Pass"
    else:
        return "Fail"