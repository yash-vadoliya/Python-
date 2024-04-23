import sqlite3
create = sqlite3.connect('mydb.dp')
# create the table student
create.execute('create table student(s_id integer,name varchar(255))')
print('table created')

