
marks =[12,56,32,98,12,45,1,4]
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Anisha,awesome!")

# enumerate () function adds a counter to an iterable and returns it in a form of enumerate object.
# This enumerate object can then be used directly in a for loop or converted into a list of tuples
#use for loop to iterate over the enumerate object