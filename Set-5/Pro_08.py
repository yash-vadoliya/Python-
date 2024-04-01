# 8. Create a numeric array and perform following operations on it: Add 2 to each elements, Subtract 3 from each element, Multiply each element with 3, Divide each element by 2, Find max and min, find the average of all elements.

from numpy import  *
arr = [10,20,30,40,50]

print('1. Addition')
print('2. Substraction')
print('3. Multiplication')
print('4. Division')
print('5. Max and Min')
print('6. Average')

choice = int(input('Enter Choice Number :'))
 
if(choice == 1):
    narr = [i+2 for i in arr]
    print('Addition : ',narr)
if(choice == 2):
    narr = [i-3 for i in arr]
    print('Substraction : ',narr)
if(choice == 3):
    narr = [i*3 for i in arr]
    print('Multiplication : ',narr)
if(choice == 4):
    narr = [i/2 for i in arr]
    print('Division : ',narr)
if(choice == 5):
    print(arr)
    print('Max Element In Array Is : ',max(arr))
    print('Min Element In Array Is : ',min(arr))
if(choice == 6):
    print('Average Of Array Is :  ',average(arr))