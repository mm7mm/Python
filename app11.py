import random
ran_comp = random.randint(1000,9999)
user_input = int(input("Enter a 4-digit PIN code: "))
if len(str(user_input)) !=4:
    print("Please enter 4 digits")
elif user_input==ran_comp:
    print("Success! PIN code matched")
else:
    print("Failure! PIN code did not match")
    print(f"The computer generatedthis PIN : {ran_comp}")
    pr