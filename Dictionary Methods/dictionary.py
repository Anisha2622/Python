# dictionary of lists
dic = {
    "Anisha": "Human being",
    "Spoon": "Object"
}
print(dic["Anisha"])

dic = {
    22: "Anisha",
    852: "Siddhi",
    456: "Sakshi"
}
print(dic[22])

# dictionary is mutable and can be changed
# it is use to store data in key value pair

info = {'name' : 'Anisha', 'age' : 22, 'city' : 'Mumbai'}
print(info)
print (info['name'])    
print(info.get('age')) # get method is used to get the value of a key
print(info.keys()) # keys method is used to get all the keys of a dictionary
# print(info.values())

for key in info.keys():
    print(info[key])