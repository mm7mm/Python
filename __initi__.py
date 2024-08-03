# -----------application one------------------------
# Define a class representing people with attributes like name, email, and language
class peple():
    def __init__(self, name, email, language):
        self.name = name
        self.email = email
        self.language = language

# Create an object representing a user and print its attributes
user1 = peple("Mohamed", "mohamed@gmail.com", "Arabic")
print(f"Name: {user1.name}\nEmail: {user1.email}\nLanguage: {user1.language}")

# ------------application two------------------------
# Define a class representing messages with attributes like sender, receiver, message, and date
class message():
    def __init__(self, sender, receiver, message, date):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.date = date

# Create an object representing a message and print its attributes
msg1 = message("Mohamed", "Ahmed", "Hello Ahmed", "2022-12-01")
print(f"Sender: {msg1.sender}\nReceiver: {msg1.receiver}\nMessage: {msg1.message}\nDate: {msg1.date}")

# ------------application three------------------------
# Define a class representing products with attributes like name, price, description, and feedback
class product():
    def __init__(self, name, price, description, feedback):
        self.name = name
        self.price = price
        self.description = description
        self.feedback = feedback

# Create objects representing products and print their attributes
prd1 = product("Apple", 10, "Apple is fruit", "Apple is good")
prd2 = product("book", 40, "Book is green", "Book is there star")
print(f"Name: {prd1.name}\nPrice: {prd1.price}\nDescription: {prd1.description}\nFeedback: {prd1.feedback}")
print(f"Name: {prd2.name}\nPrice: {prd2.price}\nDescription: {prd2.description}\nFeedback: {prd2.feedback}")

# -----------application four----------------------------
# Define a class representing a list of movies with attributes like title, director, year, and genre
class movies_list():
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre

    # Method to display movie details
    def show(self):
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Year: {self.year}")
        print(f"Genre: {self.genre}")

    # Method to display only the director's name
    def show_director(self):
        print(f"Director: {self.director}")

# Create objects representing movies and print their details
movie1 = movies_list("The Shawshank Redemption", "Drama", 1925, "Christopher Nolan")
movie2 = movies_list("Pulp Fiction", "Crime, Drama", 1994, "Quentin Tarantino")
movie3 = movies_list("The Godfather", "Drama ,Acthon", 2002, "Christopher ")

print("===========MOVIES LIST =============")
movie1.show()
print("------------------------------------")
movie2.show()
print("------------------------------------")
movie3.show()

# Change the director's name and print the movies after the modification
print("====================================")
print("Changing movies Dictionary.....")
print()
movie1.director = "Shokry Sarhan"
movie1.show()
print("------------------------------------")
movie2.director = "Ahmed Mazhar"
movie2.show()
print("------------------------------------")
movie3.director = "Mohamed Ali"
movie3.show()