class Person():
    def __init__(self , Code, name):
        self.Code = Code
        self.name = name
    def display_student_number(self):
        pass
    def Greet(self):
        self.Code = self.Code + 1

ayaan = Person("Fwk37 291", "Ayaan")
print(ayaan.name, ayaan.Code)
