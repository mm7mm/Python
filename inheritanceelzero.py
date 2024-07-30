class food:
    def __init__(self,name,price):
        super().__init__(self,name,price)
        # self.name=name
        # self.price=price
        print(f"{self.name} Is created form bade Class and price is {self.price}")
    def eat(self):
        print(f"Fat Metbod from Bade Class")


class apple(food):
    def __init__(self, name,price):
        # super().__init__(name,price)
        self.name=name
        self.price=price+20
        print(f"{self.name} is created from derivd class and price is {self.price}")
    
food_two=apple("pizza",50)
food_two.eat()
