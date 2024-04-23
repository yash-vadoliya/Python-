import sqlite3

crt = sqlite3.connect('mydb.dp')

crt.execute("""delete from student where s_id = 1""")

data = crt.execute('select * from student')

for i in data:
    print(i)
    