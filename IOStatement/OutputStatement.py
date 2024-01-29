#Input Output Statement
print('Yash')
print('This is the \n New line')
print('This is the \t New line')
print('This is the' + 'New line')
a = 'Yash'
print('Name is'+a)

#Print(Variable List) Statement

a,b = 1,2
print(a,b)
print(a,b,sep='#') #sep is use to seprate value using symbol

print('Yash')
print('Vadoliya')
print('Junagadh')

#print output on the same line
#end parametrer is use to print output in same line
print('Yash',end='') 
print('Vadoliya',end='')
print('Junagadh')

print('Yash',end='\t') 
print('Vadoliya',end='\t')
print('Junagadh')

#the print object statement
a = ['a','atmiya','rajkot',10,True,10.25]
print(a)

#the print('string',variable list) statement
a=7
print(a,'The value is Printed here')
print('user has enterd',a,'as an input')

#print formatted string statement
#syntax : print('formatted string'% (variable list))
a = 1
print('value=%i'%a)
# to print more than one int value
a,b=2,25
print('A=%i,B=%i'%(a,b))
a,b,c=2,25,'Yash'
print('A=%i,B=%i,C=%s'%(a,b,c))

name = 'Yash'
print('Hi %s'%name)
print('Hi %20s'%name)
print('Hi %-20s'%name)

# We can use %c to display a single character
a = 'Atmiya'
print('The first character is %c, and Second Character is %c'%(a[0],a[1]))

# we can use %f to dispaly the float value
num = 21.2163456678
print('The Number is %f'%num)
print('The Number is %1.2f'%num)

#inside the formatted string
n1,n2,n3 = 1,2,3
print('The Number is {0},The Number is {1},The Number is {2}'.format(n1,n2,n3))

name = 'Yash'
salary = 50000
print('Hello {0},Your Salary is {1}'.format(name,salary))

