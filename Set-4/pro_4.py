# 04 accept one integer value from the user;display the length of entered number,also display thatthe entred number is of four digits or not.

no = int(input('Enter Nuymber : '))
no1 = str(no)
len = len(no1)
print('length of No :',len)

if(len == 4):
    print('Number digits is 4 digits. Number is ->',no)
else:
    print('Number digits is not 4 digits. Number is ->',no)
