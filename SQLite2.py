import sqlite3

def get_all_data():
    try:
        # Connect to Database
        db = sqlite3.connect("app.db")

        # Print Success Message
        print("Connected to Database Successfully")
        
        # Setting Up Cursor
        cr = db.cursor()
        
        # Fetch Data from Database
        cr.execute('SELECT * FROM users')
        
        # Fetch All Data
        data = cr.fetchall()
        
        # Print All Data
        print(data)
         
        # Print number of rows returned
        print(f"Database Has {len(data)} rows")
        
        # Printing Message
        print("Showing data:")
        
        # Loop On Data
        for row in data:
            print(f"User ID => {row[0]}", end=" ")
            print(f"Username => {row[1]}")
        
    except sqlite3.Error as er:
        print(f"Error Reading data{er}")
    finally:
        if(db):
            # Close Database Connectionf
            db.close()
            print("Database connection closed.")        
get_all_data()