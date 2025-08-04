def func1():
    try: 
        l = {1, 5, 6, 7}
        i = int(input(" Enter a index: "))
        print(l[i])
        return 1

    except: # catch all exceptions
        print("Some error occured")
        return 0

    finally:  # This block will run regardless of whether an exception occurred or not
        print("I am always executed")

x = func1()
print(x)