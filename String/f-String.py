letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Anisha"

print(letter.format(country, name))  # Output: Hey my name is Anisha and I am

print(f"Hey my name is {name} and I am from {country}") # f -string formatting 

price =49.09999
txt =f"For only {price:.2f} dollars!"
print(txt) 
#print (txt.format(price = 49.99))
