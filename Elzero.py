admen=["mohamed","ahmed","ali"]
name=input("Enter your name :").strip().lower()

if name in admen:
    print(f"Helow{name} ")
    opthn=input("Delet or update you name :").strip().capitalize()
    if opthn =='Updated' or 'u':
        theNewName=input("New name:")
        admen[admen.index(name)] = theNewName
        print("Name updated.")
        print(admen)
    elif opthn== "Delet" or 'd':
        admen.remove(name)
        print("Name is Delet")
        print(admen)
    else:
        print("Wrong option choosed")
else:
    print("you are Not admin")
