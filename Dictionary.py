# student = {"naam": "Himanshu", "marks": "55", "city": "Hyderabad"}

# print(student["naam"])

# for key in student:
#     print(key,student[key])

# a = {"marks": 55}
# b = {"marks": "55"}

# print(a["marks"] >= 40)
# print(b["marks"] >= 40)

# student = {"naam": "Himanshu", "marks": 55, "city": "Hyderabad"}
# print(student.get("age"))
# print(student.get("age", "pata nahi"))
# print(student.get("naam"))

# me = {"naam":"Himanshu", "company":"Cognizant", "role":"qea"}

# print(me.get("age"))
# print(me.get("age","nhi h"))
# print(me.get("naam"))


# def get_status(student):
#     if student.get("marks"):
#         return student["marks"]
#     else:
#         return "No Data"

# # print(get_status({"naam":"Himanshu", "marks":55}))
# # print(get_status({"naam":"Rahul", "marks":39}))
# print(get_status({"naam":"Amit"}))


def get_status(student):
    if "marks" not in student:
        return "No Data"
    elif student["marks"]>= 40:
        return "Pass"
    else:
        return "Fail"

# print(get_status({"naam": "Himanshu", "marks": 55}))
# print(get_status({"naam": "Rahul", "marks": 39}))
# print(get_status({"naam": "Amit"}))
# print(get_status({"naam": "Sam", "marks": 0}))



students = [
    {"naam": "Himanshu", "marks": 55},
    {"naam": "Rahul", "marks": 39},
    {"naam": "Amit"},
    {"naam": "Sam", "marks": 0},

]
5
# for s in students:
#     print(s["naam"], get_status(s))

def count_pass(Students):
        count =0
        for s in Students:

             if get_status(s)=="Pass":
                 count +=1
        return count

print(count_pass(students))
print(count_pass([{"naam": "X", "marks": 40}, {"naam": "Y", "marks": 100}]))