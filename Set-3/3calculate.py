# 3. rojkot corporation wants to make simple application to calculate water bill of rajkotians.
# water is biging delivered by the corporation on per liter charge of below:
# upto 90 liters - rs. 0/ltr
# upto 150 liters -rs. 2/ltr
# upto 250 lirers -rs. 5/ltr
# more than 250 - rs. 10/ltr
# Accept unit consumption from consumer and disply the bill amount.

li = int(input('Enter Liter Value: '))

if li>0 and li<=90:
 	print('You have Not Pay Charges..')
  
elif li>90 and li<=150:
 	li = li * 2
 	print('Your Charges Is : ',li)
  
elif li>150 and li<=250:
 	li = li * 5
 	print('Your Charges Is : ',li)
  
elif li>250:
 	li = li * 10
 	print('Your Charges Is : ',li)


