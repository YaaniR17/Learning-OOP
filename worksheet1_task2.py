"""
Cat and Dog simulation program.
"""
__author__ = "298496 Ayaan Shahzad"
__version__ = "0.0.1"
__license__ = "MIT"
# Classes:
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + " is eating.")

    def sleep(self):
        print(self.name + " is sleeping.")

    def speak(self):
        return ""


class Cat(Animal):
    def speak(self):
        return "Meow."

    def purr(self):
        return "Purrs."


class Dog(Animal):
    def speak(self):
        return "Woof."

    def bark(self):
        return "Barks."


# Code:
cat1 = Cat("Whiskers", 2)
dog1 = Dog("Tyson", 4)

print(cat1.name, "says:", cat1.speak())
print(cat1.name, "also:", cat1.purr())
cat1.eat()
cat1.sleep()

print()

print(dog1.name, "says:", dog1.speak())
print(dog1.name, "also:", dog1.bark())
dog1.eat()
dog1.sleep()
