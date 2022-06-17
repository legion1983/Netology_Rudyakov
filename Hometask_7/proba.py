# у функции open есть ряд аргументов, которые указывают режим ее работы
# - аргумент 1ый:
# r- чтение (по -умолчанию)
# w - запись
# a - запись в конец файла
# - аргумент 2ой:

from pprint import pprint
from datetime import datetime
file_name = 'data.txt'

def logger(file_name, data):
    with open(file_name, 'a') as file_obj:
        prepare_data = f'{datetime.now()} | {data}'
        file_obj.write(f'{prepare_data}\n')

logger(file_name, 'data')
logger(file_name, 'data')


#нельзя открыть файл в режиме записи, нельзя читать файл в режиме записи. Можем либо читать либо писать