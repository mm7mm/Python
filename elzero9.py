# x=-1
# if x<0:
#     raise Exception(f"you are good namber=> {x}")
# else:
#     print("NO")
# print("Hi MOhMed")
try:
    print(10/0)
except ZeroDivisionError:
    print("Cant Divide")
except NameError:
    print("Name error")