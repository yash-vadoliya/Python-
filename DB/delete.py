import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='MyPy')

mycursor = mydb.cursor()
mycursor.execute("DELETE FROM Student WHERE rollno = 4")
mydb.commit()
mydb.close()