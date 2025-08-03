a = input("Enter the number:")
print(f"Multiplication table of {a} is:")

try:  # Try block to handle potential errors
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")
# except Exception as e:
except:     # use except Exception as e to catch all exceptions
    print("Sorry some error occured")

print("Some imp lines of code")
print("End of Program")
