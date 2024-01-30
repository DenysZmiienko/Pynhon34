# Задание 1
# Создайте программу «Англо-французский словарь».
# Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.
#
dictionary = {}
def add_translation():
    english_word = input("Enter a word in English: ")
    french_translation = input("Enter French translation: ")
    dictionary[english_word] = french_translation
    print(dictionary)

def remove_translation():
    english_word = input("Enter a word in English to remove translation:")
    if english_word in dictionary:
        del dictionary[english_word]
        print(f"Translation for {english_word} deleted.")
    else:
        print("Translation not found.")

def find_translation():
    english_word = input("Enter a word in English to find a translation: ")
    if english_word in dictionary:
        print(f"{english_word}: {dictionary[english_word]}")
    else:
        print("Translation not found.")

def change():
    english_word = input("Enter a word in English: ")
    if english_word in dictionary:
        new_english_word = input("Enter a new word in English: ")
        dictionary[english_word] = new_english_word
    else:
        print('Name not found.')

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Find")
    print("3. Deleted")
    print("4. Сhange")
    print("5. Exit")

    choice = input("Enter action: ")

    if choice == '1':
        add_translation()
    elif choice == '2':
        find_translation()
    elif choice == '3':
        remove_translation()
    elif choice == '4':
        change()
    elif choice == '5':
        break
    else:
        print("Error")

for english_word, french_translation in dictionary.items():
    print(f"{english_word}: {french_translation}")

# Задание 2
# Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
# название должности, номер кабинета, skype. Требуется
# реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для хранения
# информации.

firma = {}
def add_Full_Name():
    fio = input("Enter full name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    position = input("Enter Job title: ")
    room = input("Enter room: ")
    skype = input("Enter skype: ")
    firma[fio] = {
        "Phone": phone,
        "Email": email,
        "Job title": position,
        "Poom": room,
        "Skype": skype
        }
    print(firma)

def remove_Full_Name():
    fio = input("Enter full name: ")
    if fio in firma:
        del firma[fio]
        print(f"Full_Name {fio} deleted.")
    else:
        print("Full_Name not found.")

def find_Full_Name():
    fio = input("Enter full name: ")
    if fio in firma:
        for key, value in firma[fio].items():
            print(f"{key}: {value}")
    else:
        print("Full_Name not found.")

def change_Full_Name():
    fio = input("Enter full name: ")
    if fio in firma:
        fio = input("Enter full name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        position = input("Enter Job title: ")
        room = input("Enter room: ")
        skype = input("Enter skype: ")
        firma[fio] = {
            "Phone": phone,
            "Email": email,
            "Job title": position,
            "Poom": room,
            "Skype": skype
        }

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Find")
    print("3. Deleted")
    print("4. Сhange")
    print("5. Exit")

    choice = input("Enter action: ")

    if choice == '1':
        add_Full_Name()
    elif choice == '2':
        find_Full_Name()
    elif choice == '3':
        remove_Full_Name()
    elif choice == '4':
        change_Full_Name()
    elif choice == '5':
        break
    else:
        print("Error")

for fio, phone, email, position, room, skype in firma.items():
    print(f"{fio}: {phone}, {email}, {position}, {room}, {skype}")

# Задание 3: Магазин электроники
# Вы создаете приложение для ведения учета товаров в магазине электроники. Создайте словарь,
# где ключами будут названия товаров (например, "смартфон", "ноутбук", "планшет"), а значениями – их стоимость.
# 1. Создайте словарь с несколькими товарами и их ценами.
# 2. Выведите полный список продуктов и их цен.
# 3. Напишите функцию, принимающую название товара и выводящую его цену.
# 4. Разместите возможность обновления цены товара.
# 5. Добавьте функционал для добавления новых товаров и их цен в инвентарь.
# 6. Напишите функцию для вычисления общей стоимости товаров в корзине покупателя на основе их количества.
# 7. Реализуйте функционал удаления товара под его названием.
# Помните использовать опции и проверки для обеспечения правильности ввода данных.

FIND = 1
ADD = 2
CHANGE = 3
DELETE = 4
LOOK_UP = 5
SUM = 6
EXIT = 7

def main():
    catalog = {}
    choice = 0
    while choice != EXIT:
        choice = get_menu_choice()
        if choice == FIND:
            find(catalog)
        elif choice == LOOK_UP:
            look_up(catalog)
        elif choice == ADD:
            add(catalog)
        elif choice == CHANGE:
            change(catalog)
        elif choice == SUM:
            sum(catalog)
        elif choice == DELETE:
            delete(catalog)

def get_menu_choice():
    print()
    print('Catalog phones')
    print('--------------')
    print('1. Find phone')
    print('2. Add phone')
    print('3. Change phone')
    print('4. Delete phone')
    print('5. Look up phone')
    print('6. Sum cost phones')
    print('7. Exit')
    print('--------------')
    choice = int(input('Enter action: '))
    while choice < FIND or choice > EXIT:
        choice = int(input('Enter action: '))
    return choice


def find(catalog):
    name = input('Enter phone: ')
    for name, cost in catalog.items():
        print(f"{name}: {cost}")
    print(catalog.get(name, 'Not find.'))

def add(catalog):
    name = input(' Enter model phone: ')
    cost = input('Enter cost: ')
    if name not in catalog:
        catalog[name] = cost
    else:
        print('This model phone already exists.')

def look_up(catalog):
    for name, cost in catalog.items():
        print(f"{name}: {cost}")

def change(catalog):
    name = input(' Enter model phone: ')
    if name in catalog:
        cost = input('Enter new cost: ')
        catalog[name] = cost
    else:
        print('Not find.')

def delete(catalog):
    name = input('Enter model phone:')
    if name in catalog:
        del catalog[name]
    else:
        print('Not find.')

def sum(catalog):
    sum_phone = 0
    for item in catalog.items():
        sum_phone += item['cost']
    return sum_phone

main()

# Задание 4
# Напишите программу для удаления дубликатов из словаря.
# Например, для следующего словаря:
# >>> d = {1: 1, 2: 1, 3: 2, 'test': 1}
# Вывод программы должен быть следующим:
# >>> d = {1: 1, 3: 2}

d = {1: 1, 2: 1, 3: 2, 'test': 1}
values = set()
new_d = {}
for i, v in d.items():
    if v not in values:
        new_d.update({i: v})
        values.add(v)
print("Old dictinary: ", d)
print("New dictinary: ", new_d)