# this app for a fovoret color
color=[]
add_color=input("Add the first color you like : ")
color.append(add_color)
cholse=input("Do you want to add more colors? Yes , or No. ").lower()
if cholse == "yes":
    color2=input("Add another color to the list: ")
    color.append(color2)
    print(f"Your fovoret color is: {color}")
elif cholse == "no":
    print("OK!")
    print(f"Your fovoret color is {color}")
else:
    print("Inveled choies")
    exit
