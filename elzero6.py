# a=(10,20,30,40,50,60,70)
# b=3
# # print(bin(100544545))
# # print(id(b))
# print(sum(a))
# print(round(325.454,14))
# from random import randint , random
# print(randint(100,200))
# print((random()))
# import sys
# print(sys.path)
import datetime
print(datetime.datetime.now().time().minute)
# print(dir(datetime))
print("=" * 40)
myBirthDay=datetime.datetime(1997,2,12)
datenow=datetime.datetime.now()
print(f"my day is {(datenow - myBirthDay).days} ")
print("=" * 40)
print(myBirthDay.strftime("%d/%B/%Y"))