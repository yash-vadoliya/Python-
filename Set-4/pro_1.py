# 01 Accept two integer value from user;display the number which is smaller and the number which is bigger.
a = int(input('Enter value of A ->'))
b = int(input('Enter value of B ->'))  

if(a > b):
    print('Value Of A is Big ->',a)
else:
    print('Value Of A is Small ->',a)

if(a < b):
     print('Value Of B is Big ->',b)
else:
    print('Value Of B is Small ->',b)
    