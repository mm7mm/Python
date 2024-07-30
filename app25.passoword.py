import random
import string
print("welcome to the password Generator!")
num_pass=int(input("Enter the total number of characters in the passoword: "))
num_letters=int(input("Enter the number of letters in the password:"))
num_numbers=int(input("Enter the number of numbers in the password:"))
num_symbols=int(input("Enter the number of symbols in the password:"))

if num_pass==(num_symbols+num_numbers+num_letters):
    letters=string.ascii_letters
    numbers=string.digits
    symbols=string.printable
    passoword_chars=(
    random.choices(letters, k=num_letters)+
    random.choices(numbers, k=num_numbers)+
    random.choices(symbols, k=num_symbols)
    )
    random.shuffle(passoword_chars)
    password="".join(passoword_chars)
    print("Generated Password: ", password)
else:  
    print("Invalid input. The sum of letters, numbers, and symbols doesn''t match the passwor")