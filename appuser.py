class User:
    def __init__(self, first_name ,last_name ,email, password ,status='inactive'):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status
        
# user1 = User("mohamed" , "ali" , 'mo@gmail.com' ,"454566","active")
# print(f"Name: {user1.first_name} {user1.last_name}\nEmail: {user1.email}\nPassword: {user1.password}\nStatus: {user1.status}")


def create_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    
    return User(first_name, last_name, email, password)

user1 = create_user()
print(user1.first_name)