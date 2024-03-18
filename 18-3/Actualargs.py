# # Posittional Arguments
# def conc(a,b):
# 	s = a + b
# 	print(s)
# conc('Yash','Vadoliya')
# conc('Vadoliya','Yash')
# conc('Yash') # Error
# conc('Vadoliya','Yash','L') # Error


# Keyword Arguments
# def emp(eid,name):
# 	print('Employee Id is : ',eid)
# 	print('Employee Name is : ',name)
# emp(eid='101',name='Yash')
# emp(name='Yash',eid='101')
# emp(name='Yash') # Error


# Defult Arguments
# def fun(a,b='Yash'):
# 	print('A = ',a)
# 	print('B = ',b)
# fun(a='101',b='Ram')
# fun(a='102')


# Variable Arguments
# def add(farg,*args):
# 	sum=0
# 	for i in args:
# 		sum = sum + i
# 	print('Sum =>',(farg+sum))
# add(2,5,6,1,10)
# add(2,6,7,3)
# add(2)
