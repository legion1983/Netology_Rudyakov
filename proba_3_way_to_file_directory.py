
from datetime import datetime
from time import sleep
import os
# import os импорт библиотеки для работы с путями
# os.getcwd() получение автоматически пути к текущему каталогу
# os.path.join - сбор пути к файлу
# файл заданный система создаст сама, А КАТАЛОГ НЕ СОЗДАЕТ

LOG_CATALOG_NAME = "logs"
LOG_FILE_NAME = "log.txt"
BASE_PATH = os.getcwd()
# ---------------------------------------------------------------------------
full_path = os.path.join(BASE_PATH, LOG_CATALOG_NAME, LOG_FILE_NAME)
print(full_path)

def logger(file_path, data):
    with open(file_path, 'a') as file_obj:
        prepare_data = f'{datetime.now()} | {data}'
        file_obj.write(f"{prepare_data}\n")

for i in range(30):
    logger(full_path, "data")

    print('...')

