"""
Adds 20 students and then display each student’s number, name and course using class.
"""
__author__ = "298496 Ayaan Shahzad"
__version__ = "0.0.1"
__license__ = "MIT"
# Imports
import random

# Variables
first_names = ["Ayaan", "Artin", "Liam", "Noah", "Emma", "Olivia", "Ava", "Sophia",
               "Mason", "Logan", "Lucas", "Mia", "Ethan", "James", "Isabella",
               "Amelia", "Elijah", "Harper", "Benjamin", "Sebastian"]

courses = ["Digital Software Development", "Cyber Security", "Business",
           "Health and Social Care", "Maths and English", "Games design"]

# Functions
class Person():
    def __init__(self , Code, name, ID):
        self.Code = Code
        self.name = name
        self.ID = ID

    def Greet(self):
        self.Code = self.Code + 1
        
def generate_student_objects():
    students = {}

    for i in range(1, 21):
        name = random.choice(first_names)
        ID = random.randint(100000, 999999)
        course = random.choice(courses)

        student_obj = Person(course, name, ID)
        students[f"Student{i}"] = student_obj

    return students

students = generate_student_objects()

# Code
for key, student in students.items():
    print(f"{key}: {student.ID}, {student.name}, {student.Code}")
