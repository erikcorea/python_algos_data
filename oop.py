# Object Oriented Programming in Python

###METHODS###
string = "hello"
#print(string.upper())

#cant do
#x = 1
#print(x.upper())


###CLASSES### 
"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

d = Dog("Tim", 34)
d.set_age(23)
print(d.get_name())
print(d.get_age())


d2 = Dog("Bill", 12)
print(d2.get_name())
print(d2.get_age())

print(d.add_one(5))
print(type(d))
"""

"""
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 -100
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())
"""


###INHERITANCE###

