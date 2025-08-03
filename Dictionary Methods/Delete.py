ep1 = {122:45, 123:89, 567:69, 670:69}
ep2 = {222:67, 566: 90}

del ep1() # This will raise an AttributeError because ep1 is a dictionary, not a function
del ep1 [122] # This will delete the key-value pair with key 122 from ep1
print(ep1)