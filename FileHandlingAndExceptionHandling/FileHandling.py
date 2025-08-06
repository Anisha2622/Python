f = open('myfile.txt','r') # open file in read mode
# print(f)
text = f.read()
f.close()

# write
f = open('myfile.txt','w') # open file in write mode
f.write('Hello, world!')
f.close()

# append
f = open('myfile.txt','a') # open file in append mode
f.write('Hello, world!')
f.close()

# with statement
with open('myfile.txt','r') as f: # open file in read mode
    f.write ('Hello, Everyone!')