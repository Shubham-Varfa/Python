# creating custom exception
class customError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# function that may cause a custom exception
def division(a,b):
    if b == 0:
        raise customError("Cannot devide by 0") 
    else:
        return a/b

try:
    result = division(10, 0)
except customError as e:  # a is usedto refer to the except block
    print("There is a custom error:" , e)
else:
    print("Result is", result)

class myError(Exception):
    def __init__(self, mess):
        self.mess = mess
        super().__init__(self.mess)
    
def divide(a,b):
    if b == 0:
        print("cannot devide by 0")
    else:
        return a/b

try:
    result = divide(10, 0)
except myError as a:
    print("there is a custom erroe", a)
else:
    print("result is", result)