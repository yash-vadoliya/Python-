import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='MyPy')

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM Student')
myres = mycursor.fetchall()
for i in myres:
    print(i)