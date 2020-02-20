import sqlite3
# create if does not exists and connect to a database
conn = sqlite3.connect('demo.db')
# create the cursor
c = conn.cursor()
# run an sql
c.execute('''CREATE TABLE users (username text, email text)''')
c.execute("INSERT INTO users VALUES ('me', 'me@mydomain.com')")
# commit at the connection level and not the cursor
conn.commit()
# passing in variables
username, email = 'me', 'me@mydomain.com'
c.execute("INSERT INTO users VALUES (?, ?)", (username, email) )
# passing in multiple records
userlist = [
    ('paul', 'paul@gmail.com'),
    ('donny', 'donny@gmail.com'),
]
c.executemany("INSERT INTO users VALUES (?, ?)", userlist )
conn.commit()

# passed in variables are tuples
username = 'me'
c.execute('SELECT email FROM users WHERE username = ?', (username,))
print c.fetchone()

lookup = ('me',)
c.execute('SELECT email FROM users WHERE username = ?', lookup )
print c.fetchone()
