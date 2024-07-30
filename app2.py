#Input vriapol
str_length=input("Please type length : \n")
str_width=input("Please type width : \n")
str_slary=input("How much for 1 meter? : \n")
#Convert Type 
length=float(str_length)
width=float(str_width)
slary=float(str_slary)

area=length*width
give_slary=area*slary

str_area=str(area)
str_slary=str(give_slary)

print("The total area is : " + str_area)
print("Give the guy : $" + str_slary)
