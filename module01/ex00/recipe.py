import sys

def check_name(name):
    if not name or name.isspace():
        sys.exit("Wrong parameter for name, must be a string and cannot be empty")
    if isinstance(name, str):
        return name
    sys.exit("wrong parameter for name, must be a string")

def check_cooking_lvl(cooking_lvl):
    if not cooking_lvl or cooking_lvl < 1 or cooking_lvl > 5:
        sys.exit("Wrong parameter for cooking level, must be an integer between 1 and 5, and cannot be empty")
    if isinstance(cooking_lvl, int):
        return cooking_lvl
    sys.exit("wrong parameter for cooking level, must be an integer")

def check_cooking_time(cooking_time):
    if not cooking_time or cooking_time < 0:
        sys.exit("Wrong paramter for cooking time, must be a positive integer, and cannot be empty")
    if isinstance(cooking_time, int):
        return cooking_time
    sys.exit("wrong parameter for cooking time, must be an integer")

def check_ingredients(ingredients):
    if not ingredients or ingredients.isspace():
        sys.exit("wrong parameter for ingredients, must be a non empty string")
    if isinstance(ingredients, str):
        return list(ingredients.split(","))
    sys.exit("wrong parameter for ingredients, must be a string")

def check_type(recipe_type):
    if not recipe_type or recipe_type.isspace():
        sys.exit("wrong parameter for recipe type, must be a non empty string")
    if isinstance(recipe_type, str):
        return recipe_type
    sys.exit("wrong parameter for recipe type, must be a string")

def check_description(description):
    if isinstance(description, str) or description == None:
        return description
    sys.exit("wrong parameter for description, must be a string or empty")

class Recipe:
    def __init__(self, c_name, c_cookinglevel, c_cookingtime, c_ingredients, c_recipetype, c_description=None):
        self.name = check_name(c_name)
        self.cooking_lvl = check_cooking_lvl(c_cookinglevel)
        self.cooking_time = check_cooking_time(c_cookingtime)
        self.ingredients = check_ingredients(c_ingredients)
        self.recipe_type = check_type(c_recipetype)
        self.description = check_description(c_description)
        if self.description == None:
            self.description = "No description for this meal"
    
    def __str__(self):
        """Return the string to print with the recipe info"""
        ingredients_list = ','.join(self.ingredients)
        txt = (f' - {self.name}\n'
               f' - the difficulty to make it is {self.cooking_lvl} out of 5\n'
               f' - it takes {self.cooking_time} minutes to bake\n'
               f" - In order to make it, you'll need : {ingredients_list}\n"
               f' - it is a {self.recipe_type}\n'
               f' - {self.description}\n') 
        return txt