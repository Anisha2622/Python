x = int(input("Enter value of x:"))
# x is the variable to match 
match x:
    # if x is 0
    case 0:
        print("x is 0")
    # case with if condition
    case 4:
        print("case is 4")

# also we can use multiple cases
#alos use if statement 
    case _ if x!=90:
        print("x is not 90")
    case _ if x!=80:
        print("x is not 80")

    case _:
        print(x)
