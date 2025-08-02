# a = 9
# b = 8
# gmean1 = (a*b)/(a+b) # Geometric mean of two numbers
# print(gmean1)
# c = 8
# d = 7
# gmean2 = (c*d)/(c+d) # 
# print(gmean2)


###// Geometric Mean and greater than or equal to condition
# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print (mean)

# a = 9
# b = 8
# if(a>b):
#     print(" First is greater")
# else:
#     print("Second is greater or equal")
# calculateGmean(a,b)
# c = 8
# d = 74
# if(c>d):
#     print("First is greater")
# else:
#     print("Second is greater or equal")
# calculateGmean(c,d)  

### ///using function

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print (mean)

def isGreater (a,b):
    if a > b:
        print("first number is greater")
    else:
        print("second number is greater or equal")

def islesser(a,b):# lesser function
    pass  # pass is a placeholder when you want to do nothing

a = 9
b = 8
isGreater(a,b) # calling the function
calculateGmean(a,b) # calling the function
c = 8
d = 74
isGreater(c,d)
calculateGmean(c,d)