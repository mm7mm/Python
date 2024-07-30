#import SQlite Model
import sqlite3

#create database and connect to database
db = sqlite3.connect('app.db')

#create cursor object
cr = db.cursor()


#Update Database
cr.execute("update users set name ='Gmal' where user_id =1")
cr.execute("update users set name ='Ali' where user_id =2")
cr.execute("update users set name ='Ameer' where user_id =3")

#Delete Data
# cr.execute("delete from users where user_id =1          ")

#fetch Data
cr.execute("select * from users")
 
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

#save commit changes
db.commit()