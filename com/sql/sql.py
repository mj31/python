import sqlite3

db = sqlite3.connect("test.db")
cursor = db.cursor()
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
cursor.execute('select * from  user')
values = cursor.fetchall()
print(values)
cursor.close()
db.close()
