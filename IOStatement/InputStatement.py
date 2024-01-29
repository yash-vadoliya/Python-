# Input Statement

a = input()
print(a)

name = input('Enter Your Name :')
print(name)

#Restring The Input
sal = int(input('Enter Your Salary : '))
print(sal)

# Only Second Character will be stored in the variable
char = input('Enter Character:')[1]
print(char)

# use of split() method
# When the user Enters Multipale Values,There Are accepted as string.
# this Strings are devided wheraver space is found by split function
# using split() to accept 3 values from the user and display the sum of three values
n1,n2,n3 = [int(no) for no in input('Enter 3 Int Value By Giving Space : ').split()]
print('The Sum Of Enter Digits:',n1+n2+n3)

n1,n2,n3 = [int(no) for no in input('Enter 3 Int Value By Giving Comma : ').split(',')]
print('The Sum Of Enter Digits:',n1+n2+n3)

