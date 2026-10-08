class Person():
    def __init__(self , Code, name):
        self.Code = Code
        self.name = name
    def Greet(self):
        self.Code = self.Code + 1
    def setCourseId(self, new_course_id):
        self.Code = new_course_id
ayaan = Person("Fwk37 291", "Ayaan")
print(ayaan.name)
print(ayaan.Code)
new_id = "Fwk37 292"
ayaan.setCourseId(new_id)
print(f"\nNew CourseId: {ayaan.Code}")
