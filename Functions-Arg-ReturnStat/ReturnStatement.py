# Return statement
# The return statement is used to exit a function and return a value to the caller. The syntax is

def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    # return 7  
    return sum/len(numbers)# return the average of the numbers

c = average(5, 6, 7, 1)  # call the function with arguments 5, 6, 7, 1
print(c) # prints the average of the numbers 5, 6, 7, 1