# variable length arguments

def average(*numbers): # * is used to unpack the arguments
    #print(type(numbers))
    sum = 0
    for i in numbers: # loop through the numbers
        sum = sum + i # add the numbers to the sum
    print("Average is: ", sum/len(numbers)) # calculate average
average(5,6,7,1)
# in this case, the function can take any number of arguments, and they are all stored in the numbers variabl
# and also arguments is tuple , so we can use tuple methods on it


## 2. Keyword arguments dictionary type
def name(**name):
    #print(type(name))
    print("Hello", name["fname"],name["mname"], name["lname"])

name(mname = "mohamed",lname = "Barnes", fname = "ali") # this is how we call the function with keyword