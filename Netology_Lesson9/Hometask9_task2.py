# -----------------------------------task_2_yandex--------------------------------------

import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = "AQAAAAAAGUQeAADLW859Tk4gikBEmkURmI0u8H0"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def create_folder(path):
    requests.put(f'{URL}?path={path}', headers=headers)

create_folder('Netology_new')

def upload_file(loadfile, savefile, replace=False):
    res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    with open(loadfile, 'rb') as f:
        try:
            requests.put(res['href'], files={'file':f})
        except KeyError:
            print(res)

upload_file(r'C:\Users\daria\OneDrive\Документы\GitHub\Netology_new\Netology_Lesson9\test.txt', 'Netology_new/test.txt')