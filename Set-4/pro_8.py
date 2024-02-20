# 08 Accept one integer value from user; display the table of it.

no = int(input('Enter a number: '))

for i in range(1,11):
    print(no,'X',i,'=',no*i)