# 10. Accept numeric elements from the user, store it to the array and display. Ask user to enter search element. Display the position of the searched element.

from array import*

ar=array('i',[])
no=int(input('Enter number of elements you want to enter :'))

for i in range(no):
	ar.append(int(input('Enter any value : ')))
x=int(input('Enter value to search in element : '))

for i in range(no):
	if ar[i]==x:
		print('The element is present in the array at position :',i,'And the value is : ',ar[i])