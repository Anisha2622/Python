# constructors
class person:
    def __init__(self, name, occ):  # constructor
        print("Hey I am Person")
        self.name = name
        self.occ = occ

    def info (self):   # method
        print(f"{self.name} is a {self.occ}")


a = person("John", "Engineer")
# access attributes
b = person("Jane", "Doctor")
# access attributes
a.info()
b.info()

# print(a.name) 
