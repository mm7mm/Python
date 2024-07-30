import sqlite3

# Create Database and connect
db = sqlite3.connect("app.db")

# Setting Up the cursor
cr = db.cursor()

# Create The Tables and Fields
cr.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER, 
    name TEXT
)
""")
cr.execute("""
CREATE TABLE IF NOT EXISTS skills (
    name TEXT, 
    progress INTEGER, 
    user_id INTEGER
)
""")

# Inserting Data
my_list = ['Ahmed', 'Sayed', 'Mohamed', 'Ali', 'Kamal', 'Sameh', 'Enas']
for key, user in enumerate(my_list, start=1):
    cr.execute(f"INSERT INTO users (user_id, name) VALUES ({key}, '{user}')")


cr.execute('select * from users')

# print(cr.fetchone())
print(cr.fetchall())
# print(cr.fetchmany(2))

# Save (commit) changes
db.commit()

# Close Database
db.close() 

