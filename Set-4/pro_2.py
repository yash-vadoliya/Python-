# 02 Accept one integer value from user;check wheter enterd number is divisible by 5 or not.

no = int(input('Enter Number :'))
if(no % 5 == 0):
    print('Number is divisible by 5 and Number is ->',no)
else:
    print('Number is not divisible by 5 and Number is ->',no)