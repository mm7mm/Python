list1=[1,2,3,4,5,6,7,8,9]
list2=["A","B","C","q"]
tuple1=("man","woman","boy","girls")
dict1={"man":"mohmed","woman":"MOna","boy":"Ahmed","girls":"Aya"}
# ultimet=zip(list1 , list2)

for i,x,y,z in zip(list1,list2,tuple1,dict1):
    print(f"List1 Item =>{i}")
    print(f"List2 Item =>{x}")
    print(f"Tuple1 Item =>{y}")
    print(f"dict1 Item =>{z} the valy is => {dict1[z]}")