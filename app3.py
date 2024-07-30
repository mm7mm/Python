total_minutes=input("Please typ the nummper of minutes : \n")
int_minutes=int(total_minutes)
hour=int_minutes //  60
minutes=int_minutes %  60
print("The course is : " + str(hour) +"Hours and " + str(minutes) + " minutes long")
