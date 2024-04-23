import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='MyPy')

m_c = mydb.cursor()
m_c.execute('CREATE TABLE Student (rollno int,name varchar(255))')