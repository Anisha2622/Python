
def my_generator():
    for i in range(50000000):  
        # complex computation 
        yield i     # yield is used to produce a series of results over time

gen = my_generator()  # Create a generator object
# print(next(gen)) 
# print(next(gen))
# print(next(gen)) 

for j in gen:  # This will print all numbers from 0 to 49999999
    print (j)

