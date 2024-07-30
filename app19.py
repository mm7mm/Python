import random
paper="📜"
scissors="✂️"
rock="✋"
print("Welcome to the Rock,Paper, Scissors game: ")
help=(input("Press Enter to continue or type (Hlep) for the rules: ")).lower()
if help=="help":
    print("""
**********RULES************
1) You choose and the computer chooses
2) Rock smashes Scissors -> Rock wins
3) ScissosCut Paper -> Scissor swin
4) Paper covers Rock ->Paper wins
""")
else:
    print("Pleas Enter Help")
    exit
choose=input("Enter your choice(rock, paper, scissors): ").lower()
# choose_com=random.randint(1 ,3)
# if choose=="paper":
#     choose=paper
#     if choose_com==1:
#         choose_com=scissors
#         print(f"You chose :\n {choose}\n Computer chose:\n {choose_com}")
#         print("You lose .sissors beats paper")
#     elif choose_com==2:
#         choose_com=paper
#         print(f"You chise :\n {choose}\n Computer chose:\n {choose_com}")
#         print("You twin ")
#     else:
#         choose_com=rock
#         print(f"You chise : \n{choose}\n Computer chose:\n {choose_com}")
#         print("You win")


# elif choose=="scissors":
#     choose=scissors
#     if choose_com==1:
#         choose_com=scissors
#         print(f"You chose :\n {choose}\n Computer chose:\n {choose_com}")
#         print("You twin")
#     elif choose_com==2:
#         choose_com==paper
#         print(f"You chise : \n{choose}\n Computer chose:\n {choose_com}")
#         print("You win ")
#     else:
#         choose_com=rock
#         print(f"You chise :\n {choose}\n  Computer chose: \n{choose_com}")
#         print("You lose .sissors beats paper")


# elif choose=="rock":
#     choose=rock
#     if choose_com==1:
#         choose_com=scissors
#         print(f"You chose :\n {choose}\n Computer chose: \n{choose_com}")
#         print("You win")
#     elif choose_com==2:
#         choose_com=paper
#         print(f"You chise :\n {choose}\n Computer chose: \n{choose_com}")
#         print("You lose ")
#     else:
#         choose_com=rock
#         print(f"You chise :\n {choose}\n Computer chose:\n {choose_com}")
#         print("You twin")
# else:
#     print("Invalid choice. Please run the program again and chose rock, paper, or scissors.")


# طريقة اخري لحل
#user choose
if choose not in ['rock' ,'paper','scissors']:
        print("Invalid choice. Please run the program again and chose rock, paper, or scissors.")
else:
        if choose=="rock":
                print(f"\n You choose :\n{rock}")
        elif choose=="paper":
                print(f"\n You choose :\n{paper}")
        else:
                print(f"\n You choose :\n{scissors}")

# computer choose
choose_com=random.choice(['rock' ,'paper','scissors'])
if choose_com=="rock":
        print(f"\n You  computer choose :\n{rock}")
elif choose_com=="paper":
        print(f"\n You  computer choose :\n{paper}")
else:
        print(f"\n You  computer choose :\n{scissors}") 

#Determine the winner
if choose== choose_com:
        print("It's a tie!")
elif (
        (choose=="rock" and choose_com=="scissors")
        or
        (choose=="paper" and choose_com=="rock")
        or
        (choose=="scissors" and choose_com=="paper")
):
        print(f"You win! {choose} beats {choose_com}")
else:
        print(f"You lose! {choose_com} beats {choose}")
        

        
        