import sqlite3

crt = sqlite3.connect('mydb.dp')

crt.execute("""update student set name='mukesh' where s_id = 3""")

data = crt.execute('select * from student')

for i in data:
    print(i)
    