import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root",passwd="", db="")
c = conn.cursor()
c.execute("CREATE DATABASE testdb ")
c.execute("USE testdb ")
c.execute("CREATE TABLE users (username VARCHAR(50),  email VARCHAR(50) )  ")
userlist = [
    ('paul', 'paul@gmail.com'),
    ('donny', 'donny@gmail.com'),
]
# this is where it's different from the sql lite module for example
c.executemany("INSERT INTO users VALUES (%s, %s)", userlist )
conn.commit()
c.execute("SELECT * FROM users")
for row in c.fetchall():
    print row

conn.close()
