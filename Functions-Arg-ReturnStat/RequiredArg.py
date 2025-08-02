# Required Arguments 

def average(a , b, c=1):# c is optional argument with default value 1
    print("The average is ",(a+b+c)/2)
average(5,6) # c is not provided, so it will take default value 1

def name(fname , mname, lname):# fname, mname, lname are required arguments
    print("Hello,",fname,mname,lname)
name("John","Doe","Smith") # all required arguments are provided if not it will throw an error