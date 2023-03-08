from pprint import pprint


def make_cook_book(recipes_filename='recipes.txt'):
    with open(recipes_filename) as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredient_count = int(file.readline())
            ingredient = []
            for _ in range(ingredient_count):
                ing = file.readline().strip()
                ingredient_name, quantity, measure = ing.split(' | ')
                ingredient.append(
                    {
                        'ingredient_name': ingredient_name,
                        'quantity': int(quantity),
                        'measure': measure
                    }
                )
                cook_book[dish_name] = ingredient
            file.readline()
        return cook_book


# pprint(make_cook_book(), sort_dicts=False)

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for recipe in dishes:
        ingredients = cook_book[recipe]
        for ingredient in ingredients:
            if shop_list.get(ingredient['ingredient_name']):
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }

    return shop_list


pprint(get_shop_list_by_dishes(make_cook_book(), ['Запеченный картофель', 'Омлет'], 2))



