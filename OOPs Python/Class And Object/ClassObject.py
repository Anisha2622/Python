
class person:
    name = "Anisha"
    occupation ="Software Engineer"
    networth =10

# Accessing attributes
    def info(self): # self is a reference to the instance of the class
        print(f"{self.name} is a {self.occupation}")

a = person()
a.name = "Siddhi"
a.occupation = "Accountant"
# print(a.name,a.occupation)
a.info()
