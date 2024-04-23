import sqlite3

crt = sqlite3.connect('mydb.dp')

crt.execute('''INSERT INTO STUDENT VALUES(1,'yash')''')
crt.execute('''INSERT INTO STUDENT VALUES(2,'Abhi')''')
crt.execute('''INSERT INTO STUDENT VALUES(3,'Dhaval')''')

print('Record Insert Successfully')
crt.commit()
