import re
email_input=input("Please write your Email: ")
search =re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net" , email_input)
empty_list=[]
if search !=[]:
    empty_list.append(search)
    print("Email Added")
else:
    print("Invalid Email")

for email in empty_list:
    print(email)