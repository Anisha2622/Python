# Parameterized constructor
class Details: # class name
    def __init__(self, animal, group): # constructor
        self.animal = animal            # instance variable
        self.group = group             # instance variable

obj1 = Details('Lion', 'Predator')     # object creation
print (obj1.animal, "belongs to the", obj1.group, "group")  # accessing instance variables

# parameterized constructor is used to create an object with a set of values
# it is used to initialize the state of an object
