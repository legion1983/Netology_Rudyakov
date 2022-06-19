# менеджер контекста всего навсего открывает и закрывает ресурс сам. Решает проблему незакрытых файлов
# Методы чтения файлов:
# read - чтение файла целиком (жрет много памяти)
# readline - прочтение построчное (если нет достаточно памяти и если большие файлы)
# readlines - чтение всех строк в список (редко используют)
# по умолчанию считывание открытых файлов идет в виде строк

# --sample N1 for read--

# file_name = "shop.txt"
# def catalog_reader(file_name: str) -> dict:
#   with open(file_name, 'r', encoding="utf-8") as file:
#       data = file.read()
#       print(file.closed)
#   print(data)
#
#
# catalog_reader(file_name)

# --sample N2 for readline--

# выполняя команду readline мы принудительно убираем линию из файла при чтении (это надо учитывать)
# file_name = 'shop.txt'
# def catalog_reader(file_name):
#     with open(file_name, 'r', encoding="utf-8") as file:
#         line = file.readline()
#         print(line)
#         print("")
#         print(file.read())
# catalog_reader(file_name)

# --sample N3 for readlines--

# file_name = 'shop.txt'
# def catalog_reader(file_name):
#     with open(file_name, 'r', encoding="utf-8") as file:
#         lines = file.readlines()
#         for line in lines:
#             print(line)
#
# catalog_reader(file_name)

# --sample N4 for итерирование по циклу сразу, без readlines--
# strip метод обрезает нам пустые строки
# file_name = 'shop.txt'
# def catalog_reader(file_name):
#     with open(file_name, 'r', encoding="utf-8") as file:
#         for line in file:
#             print(line.strip())
#
# catalog_reader(file_name)

# --sample N5 словарь делаем--
# интересно потрошим файл по циклу, ВРОДЕ ЦИКЛ, НО К КАЖДОЙ СЛЕДУЮЩЕЙ СТРОЧКИ НОВОЕ ДЕЙСТВИЕ ДЕЛАЕМ ПО ТАКОМУ ЦИКЛУ
file_name = 'shop.txt'
from pprint import pprint
def catalog_reader(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        result = {}
        for line in file:
            shop_name = line.strip()
            goods = []
            for item in range(int(file.readline())):
                good = file.readline()
                goods.append(good.strip())
            result[shop_name] = goods
            file.readline()
# фейковое чтение чтобы убрать строку пустую file.readline()
        return result
catalog = catalog_reader(file_name)
pprint(catalog)