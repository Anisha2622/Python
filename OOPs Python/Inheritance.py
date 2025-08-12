# Inheritance in Python 
# Inheritance is a mechanism in object-oriented programming (OOP) that allows one class to inherit
# properties and methods from another class. The class that is being inherited from is called 
# the parent class or the superclass, and the class that is doing the inheriting is called 
# the child class or the subclass.
class  employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of employee: {self.id} is {self.name}")

class Programmer(employee):
    def showLanguage(self):
        print("The default language of programmer is Python")
        