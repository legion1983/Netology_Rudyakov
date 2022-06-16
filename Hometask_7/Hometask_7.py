file_name = 'data.txt'
def catalog_reader(file_name):
    with open(file_name, encoding='utf8') as file_obj:
        for line in file_obj:
            shop_name = line
            print(f'Shop - {shop_name}')
            quantity = file_obj.readline()
            for item in range(int(quantity)):
                print(f'Item - {file_obj.readline()}')
#фейковое чтение строки с пробелом
            file_obj.readline()


catalog_reader(file_name)

# Распарсить!!! ВАУ!!!
#
#
# _Python__
#
# file_name = 'data.txt'
#
#
# def catalog_reader(file_name: str) -> dict:
#     # step 1 - opening
#     file = open(file_name)
#     print(type(file))
#
#     # step 2 - получить данные
#     data = file.read()
#     print(type(data))
#     print(data)
#     # step 3 - закрытие файла
#     file.close()
#
#
# catalog_reader(file_name)
#
#
# # менеджер контекста (with)
# def catalog_reader(file_name: str) -> dict:
#     # step 1 - opening
#     with open(file_name) as file:
#         # читается как - при помощи функции open открой файл и помести его в переменную file
#         print(f'1 - {file.closed}')
#         data = file.read()
#     print(f'2 - {file.closed}')
#
#
# # получение линии line
# def catalog_reader(file_name: str) -> dict:
#     with open(file_name) as file:
#         # line принудительно забирает первую строку и дальше файл остается без этой первой строки
#         line = file.readline()
#         print(line)
#         print(file.read())
#
#
# # получение список 1
# def catalog_reader(file_name: str) -> dict:
#     with open(file_name) as file:
#         # readlines принудительно делает список строк
#         lines = file.readlines()
#         print(lines[-1])
#
#
# # получение список 2
# def catalog_reader(file_name: str) -> dict:
#     with open(file_name) as file:
#         # readlines принудительно делает список строк
#         for line in file:
#             print(line.strip())
# # strip -убрал все незначащие пробелы в начале и конце строк
#
# Магазин 1
# 2
# Товар_1_1 | 1 | 2 | 1000
# Товар_1_2 | 2 | 3 | 1900
#
# Магазин 2
# 3
# Товар_2_1 | 1 | 4 | 1009
# Товар_2_2 | 2 | 5 | 1500
# Товар_2_3 | 3 | 2 | 2000
#
# Магазин 3
# 1
# Товар_3_1 | 1 | 7 | 3000
