# classes and methods # OOPS

class Marks:
    marks = 0 #default

class Subjects:
    sub1 = "Computer Science"
    sub2 = "Math"
    sub3 = "Physics"

class Faculty (Subjects):
    college_name = "Acropolis"
    
    def __init__(self, _id, name, age):
        self._id = _id
        self.name = name
        self.age = age

class Student (Marks, Subjects):
    college_name = "Acropolis"

    @classmethod #decorator
    def student_marks(cls):
        cls.marks = 80

    @staticmethod #decorator
    def hello_student():
        print("Hello student")

    def __init__(self, _id, name, age):
        self._id = _id
        self.name = name
        self.age = age


f1 = Faculty("TERG80034", "Tenny", 34)
print(f1.college_name, f1._id, f1.name, f1.age, f1.sub3)

s1 = Student("DPVT20214", "Adam", 22)
s1.hello_student()
print(s1. college_name, s1._id, s1.name, s1.age, s1.sub1, s1.sub2, s1.sub3)
