import random
ran=random.randint(0,10)
num=int(input("GUESS A NUMBER BETWEN 1 and 10 : "))
while num!=ran:
    if num>=6:
        print("Too high! Guess again: ")
        num=int(input("GUESS A NUMBER BETWEN 1 and 10 : "))
    else:
        print("Too low! Guess again") 
        num=int(input("GUESS A NUMBER BETWEN 1 and 10 : "))
print("CONGRATULATIONS! you gues the numbe!")


