#ZeroDevisionError
#ValueError
#SyntexError
#KeyError
#IndexError
#FileNotFounderror

# try:
#     a = 5/int(input("Enter a number: "))
#     print(a)
# except ValueError:
#     print("Error: Invalid input. Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Cannot devide by Zero")
# else:
#     print("result is", a)
# finally:
#     print("Program End....")

# File handeling
import os
with open ('/home/mypc/Documents/Python/demo-1', 'w') as f:
    data = f.write('Welcome to GammEdge')
    print(data)

