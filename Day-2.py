import mymodule as md #this is an imported user defined alias module
import platform
md.welcome("Shubham")

#list comprehension 
numbers = [1,2,3,4,5,6,7,8,9,10]
even_num = [x for x in numbers if x % 2 == 0]
print(even_num)

#tuple manipulation
tup = (2,4,6,7,10)
#tup[3] = 8            #Error         
print(tup)

#nested dictionaries
location = {
    "country" : {
        "India" : {
            "state1" : "MP",
            "state2" : "UP",
            "state3" : "MH"
        },
        "America" : {
            "state1" : "Los Angilis",
            "state2" : "New York",
            "state3" : "california"
        }
    }
}

print(location)

# sets operations in python
set1 = {10, 20, 30}

set2 = {30, 40, 50}

union = set1.union(set2)
print(union)

intersection = set1.intersection(set2)
print(intersection)

difference = set1.difference(set2)
print(difference)

# Function
def sum_fun(a, b=10):  # Function Defination: Parameters (default parameter = 10)
    return a + b

sum = sum_fun(5)       # Function call: Arguments
print(sum)

# lambda
add = lambda x, y: x + y

result = add(500,75)
print(result)

# Built in module in Python
x = platform.system()
print(x)