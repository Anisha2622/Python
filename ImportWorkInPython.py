from math import sqrt,pi # import sqrt and pi from math module because we are using them in our code

result = sqrt(9)*pi # sqrt is square root, pi is a constant approximately equal to 3.14
print(result) 

# importing everything 

from math import * # * is a wildcard that imports all functions from math module
result = sqrt(9)*pi
print(result) 

# as keyword

from math import pi, sqrt as s  # we can also import functions with alias name
import math as m # as use for alias name
result = sqrt(9)*m.pi
print(result) 

#dir function 
import math
print(dir(math)) # dir function returns a list of all the functions and variables in the module
