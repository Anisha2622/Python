#append method

l = [11, 45, 1, 2, 4, 6]
print(l)
l.append(7) # append 7 to the end of the list
print(l)

# sort method

l = [11, 45, 1, 2, 4, 6]
print(l)
l.sort() # sort the list in ascending order
l.sort(reverse=True) # sort the list in descending order
print(l)

# reverse method 
l = [11, 45, 1, 2, 4, 6]
print(l)
l.reverse()
print(l)

# index method
l = [11, 45, 1, 2, 4, 6]
print(l)
print(l.index(1))
print(l)

# count method
l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
print(l.count(1))
print(l)

# copy method

l = [11, 45, 1, 2, 4, 6]
print(l)
m = l.copy()
m[0] = 0
print(l)

# insert method 
l = [11, 45, 1, 2, 4, 6, 1 ,1]
print(l)
l.insert(1,899)
print(l)

# extend method

l = [900, 1000, 1100]
k = l + m
print(k)
# l.extend(m)
print(l)