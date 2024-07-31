#import SQlite module
import sqlite3

#create a new database or connect to an existing one
db.sqlite3.connect("app.db")

#settings Up the Cursor
cr =db.cursor()



#commit and Close Methods
def commit_and_close():
    #commit changes
    db.commit()
    
    #close the connection
    db.close()
    print("Database connection closed.")
    