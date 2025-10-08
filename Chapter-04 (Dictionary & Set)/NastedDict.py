student = {
    "Name": "Amit sarkar",
    "Subjects": {
        "phy": 85,
        "OS": 80,
        "DBMS": 80
    }
}
# print(student)
print(student["Subjects"]["OS"])
print(student.keys())
# type_casting
print(list(student.keys()))
print(len(student))
