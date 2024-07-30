# print("***Welcometothe multiplication table***")
# number=int(input("Enter a number:"))
# for i in range(1 ,13):
#     result=i*number
#     print(f"{number} * {i}= {result} ")


print("==========================")
shop=[]
sels=[]
print("*****Welcometo iShop calculator*****")
basket=int(input("How many items are there ?"))
print("Let's get to counting them....")
for i in range(1,(basket+1)):
    shop1=input(f"Please tell me the name of the item number {i}:" )
    shop.append(shop1)
    sels1=float(input(f"What is the price of {shop1} :\n$"))
    sels.append(sels1)


show=input("would you like to see your entire basket items? ").lower()
if show=="yes":
    print(f"{shop}")
elif show=="no":
    print("Ok thank you")
else:
    print("Please Enter yes or no")


show_sels=input("Wold you like to see how much it'll cose? ").lower()
if show_sels=="yes":
    print(f"{sum(sels)}")
elif show_sels=="no":
    print("Ok thank you")
else:
    print("Please Enter yes or no")
