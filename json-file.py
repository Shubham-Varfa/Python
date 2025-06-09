# import json

# # Creating json file
# x = '{"id" : 211, "Name" : "Jhon", "Age" : 30}'

# # parse json
# y = json.loads(x)

# print(y["Age"])

import json

#creating a sample json data
data = '{"Id" : 101, "name" : "Iva", "Designation" : "Software Engineer"}'

# parse json
y = json.loads(data)

print(y)