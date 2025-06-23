# import the library
import numpy as np

lst = [1,2,3,4,5,6,7,8,9,10]
arr = np.array(lst)
print(arr)
print(type(arr))

lst1 = [1,2,3,4,5]
lst2 = [2,3,4,5,6]
lst3 = [3,4,5,6,7]

array = np.array([lst1, lst2, lst3])
print(array.shape)
print(array)
print("\nIndexing in multi dimentional array")

# indexing
print(array[1:,3:])

print("\ncreating an array using numpy")
create = np.arange(0, 10, 2)
print(create)