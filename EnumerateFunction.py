
marks =[12,56,32,98,12,45,1,4]
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Anisha,awesome!")

# enumerate () function adds a counter to an iterable and returns it in a form of enumerate object.
# This enumerate object can then be used directly in a for loop or converted into a list of tuples
#use for loop to iterate over the enumerate object

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

# loop over a list and print the index and value of each item(starting from index 1)

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)