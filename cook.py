class Recipe:
    def __init__(self, name, ingredients , cooking_time, instructions):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.instructions = instructions

def display_recipe(self):
    print(f"Recipe: {self.name}")
    print(f"Ingredients: {self.ingredients}")
    print(f"Cooking Time: {self.cooking_time} minutes")
    print("Instructions:{self.instructions}")
    
def create_recipe():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients, separated by comma: ").split(",")
    cooking_time = int(input("Enter cooking time (in minutes): "))
    instructions = input("Enter instructions: ")
    
    return Recipe(name, ingredients, cooking_time, instructions)

print("Welcome to Recipe Collections")
my_recipe = create_recipe()
print("Recipe added s")

my_recipe.display_recipe()