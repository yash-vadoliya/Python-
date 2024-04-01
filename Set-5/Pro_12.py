# 12. Accept dimension of the array and its values from the user, create an array as desired.

from array import *
no = int(input("How many elements You want to enter ? "))
arr = array('i',[])
for i in range(no):
    arr.append(i)
arr2 = array('i',[])
a = len(arr)+1
arr2.append(a)
for i in range(no):
    item = int(input("Enter Index Number of the Array :"))
    for x in range(len(arr2)):
        if item==arr2[x]:
            print("Please enter valid index no.")
            item = int(input("Enter Index Number of the Array :"))
        else:
            arr2.append(item)
            
    if item>len(arr)-1:
        print("Please enter valid index no.")
        item = int(input("Enter Index Number of the Array :"))
    else:
        val = int(input("Enter Value of arr[{}] : ".format(item)))
        arr[item] = val

print(arr)