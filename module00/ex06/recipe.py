import sys

def print_recipe(recipe):
    if recipe in cookbook.keys():
        print(f' Recipe for {recipe}:\n'
              f' Ingredients list : {cookbook[recipe]["ingredients"]}\n'
              f' To be eaten for {cookbook[recipe]["meal"]}\n'
              f' Takes {cookbook[recipe]["prep_time"]} minutes of cooking'
)

def del_recipe(recipe):
    if recipe in cookbook.keys():
        del cookbook[recipe]

def add_recipe(recipe, ingredients, meal, prep_time):
    cookbook.update({recipe : {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}})

def all_recipe():
    for key in cookbook:
        print(key)

def call():
    a = input(f'Please select an option by typing the corresponding number:\n'
              f'1: Add a recipe\n'
              f'2: Delete a recipe\n'
              f'3: Print a recipe\n'
              f'4: Print the cookbook\n'
              f'5: Quit\n')
    return(a)

cookbook = {'sandwich' : {'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
                          'meal' : 'lunch',
                          'prep_time' : '10'},
            'cake'     : {'ingredients' : ['flour', 'sugar', 'eggs'],
                          'meal' : 'dessert',
                          'prep_time' : '60'},
            'salad'    : {'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
                          'meal' : 'lunch',
                          'prep_time' : '15'}
}

a = call()
while (a != '5'):
    if a == '1':
        name = input("What is the name of your recipe?\n")
        ingredients = input("What are the ingredients? plz enter them separated by commas\n")
        ingredients = ingredients.split(",")
        meal = input("What type of meal is it?\n")
        prep_time = input("What is the preparation time in minutes?\n")
        add_recipe(name, ingredients, meal, prep_time)
        a = input()
    elif a == '2':
        a = input("Usage : <recipe name>\n")
        del_recipe(a)
        a = input()
    elif a == '3':
        a = input("Usage : <recipe name>\n")
        print_recipe(a)
        a = input()
    elif a == '4':
        all_recipe()
        a = input()
    else:
        a = input(f'This option does not exist, please type the corresponding number.\n'
                  f'To exit, enter 5.\n')