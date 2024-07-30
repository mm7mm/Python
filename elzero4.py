# def say_Hello(*name):
    
#     for i in name:
#         print(f"Hello {i}")
# say_Hello("mohame" ,"Ahmed" ,"Ali")

mySkill={
'Html':"30%",
'Css':"80%",
'Js':"62%",
'C++':"70%",

}

def one():
    global x
    x=10
    print(f"You x is : {x}")
def two():
    # global x
    # x=1
    print(f"You x is : {x}")

def show_skills(**skills):
    for skell ,value in skills.items():
        print(f"{skell} ==> {value}")

# show_skills(**mySkill)
one()
two()