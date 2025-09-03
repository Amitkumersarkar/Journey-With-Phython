marks = int(input("Enter marks : "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "A-"
elif marks >= 60:
    grade = "B+"
else:
    grade = "B"

print("The grade marks of the student ->", grade)
