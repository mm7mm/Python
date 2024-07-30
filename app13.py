import random
print("""
Welcome to the Coin Guessing Game!
Choose a method to tossthe coin:
1. Using random.random()
2.Using random.randint()""")

user_input=input("Enter your choice (1 or 2) : ")
if user_input =="1":
    ran_comp = random.random()
    if (ran_comp >0.5):
        computer_result= "Tails"
    else:
        computer_result="Heads"
elif user_input=="2":
    ran_comp2=random.randint(0,1)
    if ran_comp2 ==0:
        computer_result="heads"
    else:
        computer_result="Tails"

else:
        print("Invalid choice! Please select either 1 or 2")


user_choice= input("Enter your Guess( Heads or Tails ): ").lower()
if user_choice==computer_result.lower():
    print("Congratulations! You won! ")
else:
    print("sorry, you lost!")
print(f"The computer's coin toss result was: {computer_result}")