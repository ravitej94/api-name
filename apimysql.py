from flask import Flask, request
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()
#connect to database from this flask app server
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'names'
app.config['MYSQL_DATABASE_HOST'] = 'sqldatabase.cac8b0klmmyb.us-east-2.rds.amazonaws.com'
mysql.init_app(app)
db = mysql.connect()
cursor = db.cursor()


#get method api call to get the input and provide the id
@app.route("/", methods=['GET'])
#@app.route("/")
#built a function and return the value according to the sequence
def nameid():
    #get the names already there in database
    name = cursor.execute("SELECT playername FROM hrx")
    names = [row[0] for row in cursor.fetchall()]
    # get the input from user through rest api with length of 3 otherwise ask to enter the value in 3 chars
    firstname = request.args.get('firstname', None).upper()
    if len(firstname) > 3:
       return 'Enter again firstname is greater than 3 chars'
    lastname = request.args.get('lastname', None).upper()
    if len(lastname) > 3:
       return 'Enter again lastname is greater than 3 chars'
    #get the name of the hostname and store in the list
    a = firstname+lastname
    myList =[a]
    #get the value from the list
    for row in myList:
    #check if the name is already exist in the db if yes increase the sequence if not start from 0
        if row in names:
           personalnumber = cursor.execute("SELECT personalnumber FROM hrx where playername = ('%s')" % row)
           z = str(personalnumber).zfill(5)
    #check if the sequence is greater than 5000 and show that database is full or add to the next sequence
           if int(z) < 50000:
              cursor.execute("INSERT INTO hrx (playername,personalnumber,namejersey)  VALUES ('%s','%s','%s%s')" % (row,z,row,z))
              db.commit()
              return row+z
           elif int(z) > 50000:
                return 'databese is full'
        else:
           y =str(0).zfill(5)
           cursor.execute("INSERT INTO hrx (playername,personalnumber,namejersey)  VALUES ('%s','%s','%s%s')" % (row,y,row,y))
           db.commit()
           return row+y
    # close the connection
    cursor.close()
    #close the database
    db.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True) 
