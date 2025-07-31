fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen) # show length using len() function
print(fruit[0:4])# including 0 but not 4

print(fruit[1:4]) # including 1 but not 4

print(fruit[:5])#automatically take 0

#negative slicing 
print(fruit[0:-3])# automatically run like
print(fruit[0:len(fruit)-3])

print(fruit[-3:-1])
# its 5-3=2 and 5-1 =4 likewise string starting with 2 and end on 4 2:4

# Quick quiz
nm="Anisha"
print(nm[-4:-2])
