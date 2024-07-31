#-----------------------------------------------------
#---Database => SQLite =>Create Skills App -----------
#-----------------------------------------------------

#import SQlite module
import sqlite3

#create a new database or connect to an existing one
db = sqlite3.connect("app.db")

#settings Up the Cursor
cr = db.cursor()

#commit and Close Methods
def commit_and_close():
    """Commit and close the database"""
    db.commit()  # commit changes
    db.close()  # close the connection
    print("Database connection closed.")

#My user ID
uid = 1

#Input BIg Message
input_message = """
What Do You Want To Do
"s" => Show All skills
"a" => Add New Skill
"d" => Delete A skill
"u" => Update A skill
"q" => Quit The App
Choose Option: """

#input options choose
user_input = input(input_message).strip().lower()

#command options
commands = ["s", "a", "d", "u", "q"]

#Default The Method
def show_skills():
    cr.execute(f"SELECT * FROM skills WHERE user_id = '{uid}'")
    results = cr.fetchall()
    print(f"You Have {len(results)} skills.")
   
    if len(results) > 0:
        print("Showing Skills with Progress:")
        for row in results:
            print(f"Skill => {row[0]} ", end=' ')
            print(f"Progress => {row[1]}%")
        
    commit_and_close()

def add_skill():
    sk = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"SELECT name FROM skills WHERE name = '{sk}' AND user_id = '{uid}'")
    results = cr.fetchone()
    
    if results is None:  # There's no skill with the name in the database
        prog = input("Write Skill Progress: ").strip()
        cr.execute(f"INSERT INTO skills (name, progress, user_id) VALUES ('{sk}', '{prog}', '{uid}')")
        commit_and_close()  # Commit changes if skill added
    else:  # There's a skill with the name in the database
        print("Skill already exists. You cannot add it.")
        # Ask the user if they want to add a different skill
        retry = input("Do you want to add a different skill? (yes/no): ").strip().lower()
        if retry == "yes":
            add_skill()  # Call the function again for a new skill
        elif retry == "no":
            print("Exiting the application.")
            commit_and_close()
            exit()  # Exit the program
    
def delete_skills():
    sk = input("Write Skill Name: ").strip().capitalize()
    
    cr.execute(f"DELETE FROM skills WHERE name = '{sk}' AND user_id = '{uid}'")
    
    commit_and_close()

def update_skill():
    sk = input("Write Skill Name: ").strip().capitalize()
    prog = input("Write The New Skill Progress: ").strip()
    cr.execute(f"UPDATE skills SET progress = '{prog}' WHERE name = '{sk}' AND user_id = '{uid}'")
                         
    commit_and_close()

def query_skill():
    print("Query Skill")
    commit_and_close()

#Check If Command Is Executed
if user_input in commands:
    print(f"You Chose {user_input}")
    if user_input == "s":
        show_skills()
    
    elif user_input == "a":
        add_skill()
    
    elif user_input == "d":
        delete_skills()
    
    elif user_input == "u":
        update_skill()
    else:
        query_skill()
        
else:
    print("Invalid Command!")

#-----------------------------------------------------
