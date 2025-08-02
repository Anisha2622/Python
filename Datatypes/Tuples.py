tup = (1, 2, 76, 342, 32, "green", True) # tup =(1,)# tuple with one element need end with commas

print(type(tup), tup)
print(tup[0])
print(tup[-1])
print(tup[2])

if 342 in tup:
    print("342 is in the tuple")

tup2 = tup[1:4]
print(tup2)

#negative or positive or slicing like wise list
