import sqlite3

crt = sqlite3.connect('mydb.dp')

# data = crt.execute('select * from student')

# for i in data:
#     print(i)
    
#  retrivr record with condition..

data = crt.execute('select * from student where s_id > 1')

for i in data:
    print(i)