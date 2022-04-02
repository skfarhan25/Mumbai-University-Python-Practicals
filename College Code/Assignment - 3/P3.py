class Student():

    def __init__(self, name, age, rollno, Gender, Course, Result):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.Gender = Gender
        self.Course = Course
        self.Result = Result

    def ShowData(self):
        print(f"""Student Name: {self.name}
        Age: {self.age}
        Roll No.: {self.rollno}
        Gender: {self.Gender}
        Course: {self.Course}
        Result: {self.Result}""")

stud_1 = Student("Joe Smtih", 21, 21, "M", "Bsc.I.T.", 21)
stud_2 = Student("John Doe", 19, 110, "M", "Bsc.I.T.", 80)
stud_1.ShowData()
stud_2.ShowData()