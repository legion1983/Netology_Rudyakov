cp_file = "cp1251.txt"
utf_file = 'utf.txt'

data = 'Привет мир, Hellow world'

with open(cp_file, 'w', encoding='cp1251') as file:
    file.write(data)
with open(utf_file, 'w', encoding='utf-8') as file:
    file.write(data)
