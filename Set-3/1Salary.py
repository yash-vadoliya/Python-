# 1. Get basic Salary from the employee and display the net salary by calculating the following condition:
	# Applicble TA 4%, DA 30%,HRA 15% on basic salary.Applicble 3% tax,12% pf on basic salary.

basic_salary = int(input('Enter Basic Salary : '))
print('Basic Salary :',basic_salary)
ta = (basic_salary *4)/100
print('TA :',ta)
da = (basic_salary *30)/100
print('DA :',da)
hra = (basic_salary *15)/100
print('HRA :',hra)



print('________________________')

gs = basic_salary+ta+da+hra
print('Gross Salary : ',gs)

tax = (gs *3)/100
print('Tax :',tax)
pf = (gs *12)/100
print('PF :',pf)

print('________________________')

net = gs-tax-pf
print('Net Salary : ',net)