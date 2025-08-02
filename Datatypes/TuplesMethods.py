counties = ("Spain", "Italy", "India", "England", "Germany")
temp = list(counties)
temp.append("Russia") # Add "Russia" to the end of the list
temp.pop(3)           # Remove the 4th element from the list (index 3)
temp[2] ="Finland"    # Replace the 3rd element with "Finland"
counties = tuple(temp)
print(counties)

# concatenate two tuples without converting them to list
tuple1 = ("Spain", "Italy", "India")
tuple2 = ("England", "Germany")
tuple3 = tuple1 + tuple2
print( tuple3 )  

# count method
tuple1 =(0, 1, 2, 31, 2, 3, 1, 3, 2, 3)
#res = tuple1.count(3)
# res = tuple1.index(3) # returns the index of the first occurrence of the specified value
res = tuple1.index(3, 4, 8) # returns the index of the first occurrence of the specified value starting from the specified index
print('Count of 3 in tuple1 is:',res)