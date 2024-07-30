# attendees =[]
# visit=input("Enter the names ofattendees separaated by commas:" ).split(", ")
# attendees=[visit]
# for person in attendees[0]:
#     print(person)
#     v=input("Is thisperson attending? (yes/no):").lower()
#     if v=="yes":
#         print("Attendance confirmed")
#     elif v=="no":
#         print("Attendance not confirmed")
#     else:
#         print("Enter yes or no")
#     print("=========================")
#     print()

do_it=[]
no_do_it=[]
enter=input("Enter your tasks for today sepearated by acomma:").split(", ")
for topay in enter:
    print(f'{topay}')
    do=input(f"Did you finish {topay} alredy?\n").lower()
    if do=="yes":
        print("Nice Job")
        do_it.append(topay)
    elif do=="no":
        print("Try not to put it off ")
        no_do_it.append(topay)
    else:
        print("pleas Enter yes or no")
    print("================================")

you_want=input("Do you want to see your today's progress? (YES ,No)").lower()
if you_want=="yes":
    print("************Done Tasks**************")
    print(f"{do_it}")
    print("************Ongoing Tasks**************")
    print(f"{no_do_it}")
elif you_want=="no":
    print("Ok")
else:
    print("pleas Enter yes or no")


