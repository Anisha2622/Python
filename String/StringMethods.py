# String are immutable 
a = "!!!Anisha!! !!!!!!!!!!! Anisha"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Anisha","Siddhi"))
print(a.split(" "))
blogHeading ="introduction tO js"
print(blogHeading.capitalize())
str1 = "Welcome to the console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Anisha"))

str1 = "Welcome to the console  !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the console!!!"
print(str1.endswith("to",4,10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome00"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a merry Christmas\n"#\n not printable character so it is show false
print(str1.isprintable())

str1 = "               " # using spacebar
print(str1.isspace())
str2 = "                " # using tab
print(str2.isspace())

str1 = "World Health Organization "
print(str1.istitle())
str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())