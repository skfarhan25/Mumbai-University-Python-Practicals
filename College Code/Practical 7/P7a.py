class Student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def ShowData(self):
        print(f"Student Name: {self.name}\nAge: {self.age}\nRoll No.: {self.rollno}")

stud_1 = Student("Shaikh Farhan", 18, 124)
stud_2 = Student("John Doe", 19, 110)
stud_1.ShowData()
stud_2.ShowData()