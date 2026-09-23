marks = float(input("Enter the student's marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "F"
print(f"The grade is: {grade}")