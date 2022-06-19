# Программа для кулинарной книги
# осталось только придумать как строку превратить в словарь
# sort в 3ей задаче

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
pprint(book)


