#Mini Python Project: Expense calculator
#Mini Project: Build a simple expense calculator that categorizes expenses and calculates totals

# Grocery monthly expences < 5000
# Automobile and vehicle expences p/m < 3000
# -----------------------------------------------------------------------------------------------

# Data Types
a = 10 #Int
print(a)

b = 3.14 #Float
print(b)

c = True # Boolean
print(c)

d = "This is a String"
print(d)

# Data Structures
li = ["Alex", 25, 77.70, "Indore"]   #List
print(li)

tup = ("Alex", 25, 77.70, "Indore")  #Tuple
print(tup)

dict = {                             #Dictionary
    "Name" : "Alex",
    "Age" : 25,
    "Marks" : 77.70,
    "City" : "Indore"
}
print(dict)

set = {2,3,6,8,4,1,0}                #Set
print(set)

# OPERATORS in Python

# assignment operator
x = 10
y = 5
x += y
print(x)
print(y)

# arithmetic operator
add = x + y
print(add)

# Logical operator
if 10 < 20 or 5 > 10:
    print(True)

# Comprission 
if 'ABCD' == 'DCBA':
    print("This comparision is True")
else:
    print("This comparision is False")

# Membership Operator
list = [2,4,6,8,10,12]
number = 0
if number in list:
    print("Present")
else:
    print("Not Present")

# Identity Operator
obj1 = 1000
obj2 = obj1

if obj1 is obj2:
    print("Both are same")
else:
    print("Both are not the same")

# Input in Python & Type converson
n = int(input("Enter a number: "))
print("You entered:", n)


# Loops in Python

# for range loop
print("for loop implementation")
for i in range(10):
    print(i)

# while loop
print("while loop implementation")
num = 10
while num>=0:
    if num == 5:
        break
    print(num)
    num -= 1

for num in range(100):
    pass
