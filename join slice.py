# name=input("wrte the names : ")
# names_list=name.split(", ")
# print(name[0:9:2])
# print(names_list)

# ====================================================
# names_input=input("Enter the first andlast name of your friends separated by a comma: ")
# names=names_input.split(", ")
# for i in names:
#     name=i.split()
#     print(name)
# print("Abreviated name")
# for y in names:
#     name=y.split()
#     add1=name[0][0]
#     add2=name[1][0]
#     print(f"{add1}. {add2}.")

# ======================================================
enter= input("Enter a Sentence: ").split(" ")
names=int(len(enter))
reversed_sentance=(" ".join(enter[-1 :-names-1:-1]))
print(f"reverted {reversed_sentance}")
