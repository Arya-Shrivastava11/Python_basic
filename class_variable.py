class Student:
    CollegeName='RBU'
    studentCount=0
    def __init__(self):
        self.name=''
        self.rollno=0
        Student.studentCount+=1
    def accept(self):
        self.name=input("Enter the name of the student:")
        self.rollno=int(input("Enter the roll no:"))
    def display(self):
        print(self.name)
        print(self.rollno)
    def showcount(self):
        print(Student.studentCount)


obj=Student()
obj.accept()
obj.display()
obj.showcount()
obj2=Student()
obj2.accept()
obj2.display()
obj2.showcount()