egyptian=input("are ypu egyptian? Type 'yes' or 'No'" ).lower()
if egyptian =="yes":
    print("Good ,That's the first step")
    is_18=input("Are yppu above 18 ? Type 'yes' or 'No'").lower()
    if is_18=="yes":
     print("You can have and ID")
    else:
     print("sorry ,you have to be 18 or older")
else:
  print("Sorry, an egyptian ID is give only to Egyptians")