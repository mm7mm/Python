print("""
──────██────────────██
───███▓▓█─██────██─█▓▓███
──█▒▒█▓▓██▒▒█──█▒▒██▓▓█▒▒█
──█▒▒███░█▒▒████▒▒█░███▒▒█
─████░░░░░███▓▓███░░░░░███​█
█▓▓█░░░░░░░░█▓▓█░░░░░░░░█▓​▓█
█▓▓█░░░░░░░░░██░░░░░░░░░█▓​▓█
─██░░░░░░░░░░░░░░░░░░░░░░█​█
█▒▒█░░▄██▄██▄░░▄██▄██▄░░█▒​▒█
█▒▒█░░▀██▄██▀░░▀██▄██▀░░█▒​▒█
─████░░░▀█▀░░░░░░▀█▀░░░███​█
──█▓▓█░░░░░░░░░░░░░░░░░█▓▓​█
──█▓▓█░░▀▄▄▄▄▄▄▄▄▄▄▀░░░█▓▓​█
───████░░░▄▄▄▄▄▄▄▄♥░░████
────█▒▒█░░░░░░░░░░░░█▒▒█
────█▒▒███░░░░░░░░███▒▒█
─────███▓▓█░░░░░░█▓▓███
───────█▓▓███░░███▓▓█
────────███▒▒██▒▒███
──────────█▒▒██▒▒█
───────────██▓▓██
────────────█▓▓█
─────────────██
""")
print("""
Welcometo my island!
There are two doors in front of you. a red door and a blue door""")
door=input("which door do you want to open?\n").lower()
if door=="blue":
    print("Oops! You chose the crocodile door.Game over!♻♻")
elif door=="red":
    print("Great! now you entered a room.")
    print("you found three boxes: white 😊,black 😊, green 😊") 
    color_door=input("Which box do you open? ").lower
    if color_door=="white":
        print("Oops! you opend a box filled with snakes ☠☠")
    elif color_door=="black":
        print("Oops! You openda box filled with spideers")
    elif color_door=="green":
        print("Congratulations! You found the treasure! 💰💰💰")
    else:
        print("Invalid choice! ")
else:
    print("Invalid choice!")
