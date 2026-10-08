"""
Person class to be a super class.
"""
__author__ = "298496 Ayaan Shahzad"
__version__ = "0.0.1"
__license__ = "MIT"
# Superclass
class Person:
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.ID = ID

    def displayInfo(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.ID}")


# Classes
class Student(Person):
    def __init__(self, name, age, ID, course,):
        super().__init__(name, age, ID)
        self.course = course


    def study(self):
        print(self.name + " is studying " + self.course)


class Staff(Person):
    def __init__(self, name, age, ID, job_title,):
        super().__init__(name, age, ID)
        self.job_title = job_title

    def work(self):
        print(self.name + " is working as a " + self.job_title)

# Code
student1 = Student("Ayaan", 16, 298496, "Software Development Student")
staff1   = Staff("Michael", 42, 123456, "Software Development Teacher")

student1.displayInfo()
student1.study()

print()

staff1.displayInfo()
staff1.work()
