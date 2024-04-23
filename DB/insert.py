import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='MyPy')

mycursor = mydb.cursor()

insert_query = 'INSERT INTO Student(rollno,name) VALUES(%s,%s)'
record = [(1,'yash'),(2,'Dhaval'),(3,'Abhi'),(4,'Rahul')]
mycursor.executemany(insert_query,record)

mydb.commit()
mycursor.close()
mydb.close()

