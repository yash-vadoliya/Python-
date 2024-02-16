# 5. Income Tax department wants to make an application that calculates tax on the basis of the
# income. Accept yearly income earned by the taxpayer as an input and calculate tax to be paid.
# The tax slab is as below:
# Income up to 8 lakhs – No tax
# Income more than 8 lakh and less than 10 lakhs – 15% of income
# Income more than 10 lakhs and less than 20 lakhs – 20% of income
# Income more than 20 lakhs – 30% of income

income = int(input('Enter Your Income :'))

if(income > 0 and income < 800000):
	print('You can Not Pay Tex.')
elif(income > 800000 and income < 1000000):
	tax = (income * 15 )/ 100
	print('You can Pay 15% Tex is :',tax)
elif(income > 1000000 and income < 2000000):
	tax = (income * 20)/100
	print('You can Pay 20% Tex is :',tax)
elif(income > 2000000 ):
	tax = (income * 30)/100
	print('You can Pay 30% Tex is :',tax)
else:
	print('Enter Valid Income')
