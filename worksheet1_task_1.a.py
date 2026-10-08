class Person():
    def __init__(self , ID, name):
        self.ID = ID
        self.name = name
    def display_student_number(self):
        pass
    def Greet(self):
        self.ID = self.ID + 1

ayaan = Person(298496, "Ayaan")
sarrison = Person(346892, "Sarrison")
print(ayaan.name, ayaan.ID)
print(sarrison.name, sarrison.ID)
