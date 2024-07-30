import random

# print("Welcome to 'whse wallet?'")
# print("You will give me a list of name , and I will picka person to pay ")
# names_list=input("If you're redy, enter the names swparated by a comma:")
# names=names_list.split(", ")
# length=len(names)-1
# name_number=random.randint(0,length)
# name_person =names[name_number]
# print(f"Please ask ({name_person}) to take his wallet out . Dinner is on him")



# طريقة اخرا

print("Welcome to 'whse wallet?'")
print("You will give me a list of name , and I will picka person to pay ")
names_list=input("If you're redy, enter the names swparated by a comma:").split(", ")
print(f"Please ask({random.choice(names_list)})to take his wallet out . Dinner is on him")
