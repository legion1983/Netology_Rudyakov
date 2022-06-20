# --------------------------------------Task_1_creation cook_book----------------------------------------
from pprint import pprint
file_name = "list _of_dishes.txt"
def cooking_book (file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        result = {}
        for line in file:
            dish_name = line.strip()
            ingredients = []
            for item in range(int(file.readline())):
                ingredient = file.readline().strip()
                ingredient = ingredient.split("|")
                ingredient = {'ingredient_name': ingredient[0], "quantaty": ingredient[1], "measure": ingredient[2]}
                ingredients.append(ingredient)
            result[dish_name] = ingredients
            # фейковое чтение чтобы убрать строку пустую file.readline()
            file.readline()
        return result

book = cooking_book(file_name)

# -----------------------------------------------Task_2--------------------------------------------
def get_shop_list_by_dishes(dishes, person_count):
    dict_products_for_purchusing = dict()
    for values in book.keys():
        if values in dishes:
            print(values)
            q_ty_of_ingridients = len(book[values])

            for items in range(q_ty_of_ingridients):
                weight_of_ingridients = {'measure': book[values][items]['measure'], 'quantity': person_count*int(book[values][items]["quantaty"])}
                product_name = (book[values][items]['ingredient_name'])
                dict_products_for_purchusing[product_name] = weight_of_ingridients
    pprint(dict_products_for_purchusing)
get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 2)

