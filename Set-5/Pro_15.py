# 15. Accept multiple strings and store it into the list using function.

lst = []
def insert(val):
    for i in range(no):
        item = input("Enter String {} : ".format(i+1))
        lst.append(item)
    print("List :\n",lst)
    
no = int(input("How many strings you want to enter? "))
insert(no)