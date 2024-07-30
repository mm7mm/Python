class Member:
    def __init__(self,first_name,  midle_name,   last_name,gender) :
        self.fname= first_name
        self.mname= midle_name
        self.lmame=last_name
        self.gender=gender
    def fUll_name(self):
        return f"{self.fname}{self.mname}{self.lmame}"
    def name_with_title(self):
        if self.gender=="Male":
            return f"Hello Mr {self.fname}"
        elif self.gender=="Female":
            return f"Hello Miss {self.fname}"
        else:
            return f"{self.fname}"
Member_one=Member("MOhamed ","Ali ","Mostafa","Male")
Member_tow=Member("MOhamed2","Ali","Mostafa","Male")
Member_three=Member("MOhamed3","Ali","Mostafa","Female")

print(Member_one.fUll_name())
print(Member_one.name_with_title())
