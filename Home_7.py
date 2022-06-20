# -------------------Домашнее задание к лекции «Открытие и чтение файла, запись в файл»-----------------------

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
print('')
print('------------------------Result for task 7_1------------------------------------------------')
print('')
pprint(book)
print('')
# -----------------------------------------------Task_2--------------------------------------------
def get_shop_list_by_dishes(dishes, person_count):
    dict_products_for_purchusing = dict()
    for values in book.keys():
        if values in dishes:

            q_ty_of_ingridients = len(book[values])

            for items in range(q_ty_of_ingridients):
                weight_of_ingridients = {'measure': book[values][items]['measure'], 'quantity': person_count*int(book[values][items]["quantaty"])}
                product_name = (book[values][items]['ingredient_name'])
                dict_products_for_purchusing[product_name] = weight_of_ingridients
    print('')
    print('------------------------Result for task 7_2------------------------------------------------')
    print('')
    pprint(dict_products_for_purchusing)
get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 2)
print('')


# -----------------------------------------------Task_3--------------------------------------------
print('')
print('------------------------Result for task 7_3------------------------------------------------')
file_name_1 = '7_1.txt'
file_name_2 = '7_2.txt'
file_name_3 = '7_3.txt'

def reading_files(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        number_of_string = 0
        for line in lines:
            number_of_string += 1
    # with open(file_name, 'r', encoding="utf-8") as file:
    #     lines_1 = file.readline()
    #     for line in range(number_of_string):

    return(lines, number_of_string)

reading_files(file_name_1)
reading_files(file_name_2)
reading_files(file_name_3)

dict = {file_name_1: reading_files(file_name_1), file_name_2: reading_files(file_name_2), file_name_3: reading_files(file_name_3)}
dict = {k: dict[k] for k in sorted(dict, key=dict.get, reverse=True)}


def writing_data_in_file(file_name):
    with open(file_name, 'a', encoding="utf-8") as file_obj:
        for objects in dict.items():
            print(objects)
            file_obj.write(f"File name: {objects[0]}\n Quantaty of lines: {objects[1]}\n")

writing_data_in_file("7_final_file.txt")