frout=[["Apples" ,"Bananas"] , ["milk" ,"Water"]]
print(frout)
input("Pless Enter to change the content....")
frout.append([1,2,3])
frout[0].insert(0,"Oranges")
frout[0].append("Kiwis")
frout[1].remove("Water")
frout[1].insert(0,"Coffee")
frout[1].append("Tea")
print(frout)