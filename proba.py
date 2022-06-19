# менеджер контекста всего навсего открывает и закрывает ресурс сам. Решает проблему незакрытых файлов
# Методы чтения файлов:
# read - чтение файла целиком (жрет много памяти)
# readline - прочтение построчное (если нет достаточно памяти и если большие файлы)
# readlines - чтение всех строк в список (редко используют)

file_name = "shop.txt"
def catalog_reader(file_name: str) -> dict:
    #1 Open file
    file = open(file_name)
    print(type(file))

    #2 Data recieving
    data = file.read()
    print(type(data))
    print(data)

    # File closing
    file.close()

catalog_reader(file_name)