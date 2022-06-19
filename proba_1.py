# 'W' один раз пишет в файл, а "а" дозаписывает
from asyncio import sleep
from datetime import datetime
from time import sleep
file_name = 'trash.txt'
# ------Example N1 ------
# def logger(file_name, mode, data):
#     with open(file_name, 'a') as file_obj:
#         file_obj.write(f"{data}\n")
# # \n при записи в файл, мы сами должны контролировать переход каретки на следующую строку с помощью \n
# logger(file_name, 'data')
# logger(file_name, 'data')
# logger(file_name,  'data')


# ------Example N2 ------

def logger(file_name, data):
    with open(file_name, 'a') as file_obj:
        prepare_data = f'{datetime.now()} | {data}'
        file_obj.write(f"{prepare_data}\n")

for i in range(30):
    logger(file_name, "data")
    sleep(2)

    print('...')