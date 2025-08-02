#// Basic argument argument prg

# def average(a,b):
#     print("The average is ",(a+b)/2)
# average(4,6)

#// default argument prg

def average(a=9,b=1):
    print("The average is ",(a+b)/2)
average(1,5) # direct print this line arg ingnore 1st line value in this case 
# average ()
# average(b=5) 

def name(fname, mname = "Anisha", lname = "Pawar"):
    print("Hello,",fname,mname,lname)
name( "Rahul", "Agarwal", "Jain") # here we are passing
name( "Rahul", "Agarwal")