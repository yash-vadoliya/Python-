# 1. Create a list containing several strings. Take input from the user (search string); display whether entered string is available in the list or not.

lst = ['abc', 'bcd', 'cde', 'def', 'efg']
serch = input('Enter A String you can Serch :')
if serch in lst:
    print('String is Available, String is :',serch)
else:
    print('String is not Available')
