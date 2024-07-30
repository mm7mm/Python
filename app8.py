#App 1 Passoword

print("=========================")
password=input("Enter Your Password :")
correct_password="abc"
if password ==correct_password:
    print("Password is sucsses")
else:
    print("Password is corect")



# app2 Choose
print("=========================")
typed=input("Pleas Choose (yes) , (No) Or (Maybe)\n")
if typed == "yes":
    print(f"You typed is {typed}")
elif typed == "no":
    print(f"You typed is  {typed}")
elif typed=="Maybe":
    print(f"You typed is {typed}")
else:
    print(f"You typed ({typed}) ,which is not an option \n please stick to the options")


# app3 
print("=========================")
guessed=int(input("Enter Your Nummper: \n"))
correct_number =7
if guessed == 7:
    print(f"You guessed {guessed} ,but the correct number is {correct_number}")
else:
    print("Ok Your Win")
print("=========================")
