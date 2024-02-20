# 03 accept one integer value from user;check wheter enterd number is between 0 to 100 or not

no = int(input('Enter Number : '))

if(no > 0 and no <100):
    print('Number is between 0 and 100. Number is ->',no)
else:
    print('Number is not between 0 and 100. Number is ->',no)