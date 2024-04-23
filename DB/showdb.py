import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='')

m_c = mydb.cursor()
m_c.execute('SHOW DATABASES')
for i in m_c:
    print(i)