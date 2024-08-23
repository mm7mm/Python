import os
import time

def clear_screen():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

class User:
    def __init__(self, first_name, last_name, email, password, status='inactive'):
        # Initialize user attributes
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status
        
    def display_user(self):
        # Display user information
        print(f"First name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Email : {self.email}")
        print(f"Status : {self.status}")
        print("=" * 30)

def create_user():
    # Create a new user by collecting input from the user
    first_name = input("Enter First Name : ")
    last_name = input("Enter Last Name : ")
    email = input("Enter Email : ")
    password = input("Enter Password : ")
    
    return User(first_name, last_name, email, password)

def print_all_users(users):
    # Print all users in the list
    if users:
        print("Displaying all users:")
        for user in users:
            user.display_user()
    else:
        print("No users found!")

new_users = []  # List to store new users

while True:
    print("\nWelcome to user management\n")
    print("Choose an action:\n")
    print("1 - Add new user")
    print("2 - Display all users")
    print("3 - Exit\n")
    
    choice = input("Enter your choice: ").strip()  # Using strip() to remove extra spaces
    
    if choice == '1':
        new_users.append(create_user())
        print("User added successfully")
        time.sleep(2)
    elif choice == '2':
        clear_screen()
        print_all_users(new_users)  # Call the function to print all users
        time.sleep(2)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")