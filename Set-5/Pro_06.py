# 6. Create a tuple and display it. Enter 25 at the third position and display it again.

tup = (10,20,30,40,50)

print('Orignal Tuple : ',tup)

mod_tup = tup[:2] +(25,)+ tup[2:]

print('New Tuple : ',mod_tup)