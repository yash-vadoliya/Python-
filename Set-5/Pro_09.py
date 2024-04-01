# 9. Create a numeric array and do the following: append the element, pop the element, insert an element at the desired postion, reverse the elements in the array, convert the array to list.

# Array 
from numpy import *

arr = [10,20,30,40,50]

# Append Element
arr.append(60)
print('Append Element : ',arr)

# Pop Element
arr.pop(1)
print('Pop Element : ',arr)

# Insert Element
arr.insert(1,15)
print('Insert Element : ',arr)

# Reverse Element
arr.reverse()
print('Reverse Element of Array : ',arr)

# Convert array into list
lis = list(arr)
print('Convert Array into List :',lis)
print('Type :',type(lis))