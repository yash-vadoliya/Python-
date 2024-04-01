# 7. Create a dictionary named library with following keys (Bookid, Title, Author, Price, Publisher). a. Display the dictionary, b. Display the name of Author, c.   Display the Bookid d. Display the length of the dictionary, e. Update the price, f. Insert year as the new key and display the dictionary again.

dic = {
    'bookid' : 1,
    'title' : 'Problem Solving using C Language',
    'Author' : 'Balaguru swami',
    'price' : 1000,
    'publisher' : 'Bell Leb'
}

print('1. Display Dictionary')
print('2. Display Name OF Author')
print('3. Display Bookid')
print('4. Display Length of Dictionary')
print('5. Update the price')
print('6. Insert Year of Dictionary')

choice = int(input("Enter Choice Number :"))

if (choice==1):
    print('Dictionary Is',dic)
if(choice==2):
    print('Name Of Author Is : ',dic['Author'])
if(choice==3):
    print('Book Id Is : ',dic['bookid'])
if(choice==4):
    print('Length Of Dictionary Is : ',len(dic))
if(choice==5):
    print('Book Price Is :',dic['price'])
    dic.update({'price':1500})
    print('update price of Book is : ',dic['price'])
if(choice==6):
    dic.update({'year':2024})
    print('Dictionary is : ',dic)
