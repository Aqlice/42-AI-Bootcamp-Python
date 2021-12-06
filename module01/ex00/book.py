import sys
import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        if not name or not isinstance(name, str):
            sys.exit("wrong name, must be a non empty string")
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipe_list = {'starter' : [], 'lunch' : [], 'dessert' : []}
    
    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for elem in self.recipe_list.values():
            for rec in elem:
                if rec == name:
                    print(rec)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        string = ''
        for obj in self.recipe_list[recipe_type]:
            if not string:
                string += obj.name
            else:
                string += '\n' + obj.name
        return string
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if self.recipe_list[recipe.recipe_type] is None:
            self.recipe_list[recipe.recipe_type] = recipe
        else:
            self.recipe_list[recipe.recipe_type].append(recipe)

