import sys
import MySQLdb


#Connect to DB
db = MySQLdb.connect("sqldatabase.cac8b0klmmyb.us-east-2.rds.amazonaws.com","admin","password","names" )

#Edit data of DB
cursor = db.cursor()

#Select from tables and get the current count
#number = cursor.execute("SELECT number FROM seriea")
#x =str(number +1).zfill(5)

name = cursor.execute("SELECT playername FROM seriea")
names = [row[0] for row in cursor.fetchall()]

#while numbers is not None:
#    print(numbers[0])
#    numbers = cursor.fetchone()

#Get the input for first,second name
Firstname = str(sys.argv[1])
Lastname = str(sys.argv[2])
a = Firstname+Lastname
myList =[a]

#Inserting the values into DB to keep track of number
for row in myList:
    if row in names:
       personalnumber = cursor.execute("SELECT personalnumber FROM seriea where playername = ('%s')" % row)
       z = str(personalnumber).zfill(5)
       if int(z) < 50000:
          cursor.execute("INSERT INTO seriea (playername,personalnumber,namejersey)  VALUES ('%s','%s','%s%s')" % (row,z,row,z))
          print(row+z)
       elif int(z) > 50000:
          print("databese is full")
    else:
       y =str(0).zfill(5)
       cursor.execute("INSERT INTO seriea (playername,personalnumber,namejersey)  VALUES ('%s','%s','%s%s')" % (row,y,row,y))
       print(row+y)
#    cursor.execute("INSERT INTO players (namejersey)  VALUES ('%s')" % row)
#commit to save in DB
db.commit()

#Close the seesion
cursor.close()

#Close the database session
db.close()
