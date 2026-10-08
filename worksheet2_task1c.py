"""
Handling classes with data from CSV file.
"""
__author__ = "298496 Ayaan Shahzad"
__version__ = "0.0.1"
__license__ = "MIT"
# imports
import csv
import os

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
    def __init__(self, name, age, ID, course):
        super().__init__(name, age, ID)
        self.course = course

    def study(self):
        print(self.name + " is studying " + self.course)


class Staff(Person):
    def __init__(self, name, age, ID, job_title):
        super().__init__(name, age, ID)
        self.job_title = job_title

    def work(self):
        print(self.name + " is working as a " + self.job_title)

# Manager class
class RecordManager:
    def __init__(self):
        self.records = []

    def load_from_csv(self, filename):
        
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if len(row) < 5:
                    continue

                p_type, name, age, ID, field5= row

                age = int(age)
                ID = int(ID)

                if p_type.lower() == "student":
                    new_obj = Student(name, age, ID, field5)

                elif p_type.lower() == "staff":
                    new_obj = Staff(name, age, ID, field5)
                else:
                    continue
                self.records.append(new_obj)
# Code
    def show_all(self):
        for person in self.records:
            person.displayInfo()
            if isinstance(person, Student):
                print(" Role: Student | Course:", person.course)
            elif isinstance(person, Staff):
                print(" Role: Staff | Job:", person.job_title)
            print()

manager = RecordManager()
manager.load_from_csv("people.csv")
manager.show_all()
