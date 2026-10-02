class Person:
    def __init__(self):
        self.name=''
        self.age=0
    def accept(self):
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))

    def display(self):
        print(self.name)
        print(self.age)

class Student(Person):
    def __init__(self):
        super().__init__()
        self.rollno=0
        self.branch=''
        self.marks=0
    def acceptStudent(self):
        super().accept()
        self.rollno=int(input("Enter Roll no."))
        self.branch=input("Enter branch")
        self.marks=int(input("Enter marks:"))
    def displayStudent(self):
        super().display()
        print(self.rollno)
        print(self.branch)
        print(self.marks)

obj=Student()
obj.acceptStudent()
obj.displayStudent()


