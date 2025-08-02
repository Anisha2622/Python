# Example 
marks = [90, 85, 88, "Anisha", True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])

print(marks[-3])# nagative index
print(marks[len(marks)-3])# convert positive index
print(marks[5-3])# convert positive index
print(marks[2])# access element at index 2

# check item present in this list
if "Anisha" in marks:
    print("Anisha is present in the list")
else:
    print("Anisha is not present in the list")

# same thing applies for string as well
# if "An" in "Anisha":
#     print("Yes")

print(marks)
print(marks[1:4:2])
print(marks[1:-1])

# list comprehension
list = [i*i for i in range(10)]
print(list)
list =[ i*i for i in range(10) if i%2==0]
print(list)


# # Example 1
# list1 = [1, 2, 2, 3, 5, 4, 6]
# list2 = ["Red", "Green", "Blue"]
# print( list1)
# print(list2)

# # Example 2
# details =[ "Abhijeet",18,"FYBscIT",9.8]
# print(details)