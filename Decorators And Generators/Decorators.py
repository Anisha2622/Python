
def greet(fx):
    def mfx(*args, **kwargs): # *args and **kwargs are used to pass a variable number of arguments to a function
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this functions")
    return mfx

@greet # this is a decorator for the greet function
def hello():
    print("Hello, World!")

def add (a, b):
    print(a + b)

#greet(hello()) # this will print "Good Morning", "Hello, World!", "Thanks for using this functions"
hello()
#greet(add)(1,2) # this will print "Good Morning", 3, "Thanks for using this functions"
add(1,2)