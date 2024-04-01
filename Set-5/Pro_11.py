# 11. Take two arrays enter 5 digits in both arrays. Compare the corresponding element from each array and display only the bigger number.

from numpy import *

arr1 = [1000,2000,3000,4000,5000]
arr2 = [100,200,300,400,500]


if max(arr1) > max(arr2):
	print(max(arr1))
else:
	print(max(arr2))