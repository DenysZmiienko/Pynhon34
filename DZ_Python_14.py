# Задание 1
# Есть некоторый словарь, который хранит названия
# стран и столиц. Название страны используется в качестве
# ключа, название столицы в качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку
# данных (используя упаковку и распаковку).

import os
import json

# def create_path(file_name):
#     script_dir = os.path.dirname(os.path.realpath(__file__))
#     print(script_dir)
#     return os.path.join(script_dir, file_name)
#
# def serialize_json(file_name, data):
#     path = create_path(file_name)
#     with open(path, 'w') as file:
#         json.dump(data, file, indent=4, ensure_ascii=False)
#
# def deserialize_json(file_name):
#     path = create_path(file_name)
#     with open(path, 'r') as file:
#         data = json.load(file)
#     return data
#
# try:
#     file_name = 'db.json'
#     data_base = {"Italy": "Rome", 'Spain': "Madrid", "Germany": "Berlin"}
#     serialize_json(file_name, data_base)
#     deserialized_employee = deserialize_json(file_name)
#     print(deserialized_employee)
# except Exception as e:
#     print(e)
#
# def add_json():
#     print("Adding Data to the Dictionary")
#     data = json.load(open("db.json"))
#     country = input("Country: ")
#     capital = input("Capital: ")
#     if country not in data:
#         data[country] = capital
#     else:
#         print('This country already exists.')
#     with open("db.json", "w") as file:
#         json.dump(data, file, indent=4, ensure_ascii=False)
#     print("Data added to dictionary")
#
# def del_json():
#     print("Removing data from a dictionary")
#     data = json.load(open("db.json"))
#     country = input("Country: ")
#     if country in data:
#         del data[country]
#     else:
#         print('Not find.')
#     with open("db.json", "w") as file:
#         json.dump(data, file, indent=4, ensure_ascii=False)
#     print("Data copied from dictionary")

# def change_json():
#     print("Changing Dictionary Data")
#     data = json.load(open("db.json"))
#     country = input("Country: ")
#     if country in data:
#         new_data_base = {input("Country"): input("Capital"),}
#         data[country] = new_data_base
#     else:
#         print('Not find.')
#     with open("db.json", "w") as file:
#         json.dump(data, file, indent=4, ensure_ascii=False)
#     print("Data replaced in dictionary")

# def look_up():
#     print("Show file details")
#     data = json.load(open("db.json"))
#     with open("db.json", "w") as file:
#         json.dump(data, file, indent=4)
#         for country, capital in data.items():
#             print(f"{country}: {capital}")
#
# while True:
#     print('Data_Base')
#     print('--------------')
#     print('1. add_json')
#     print('2. del_json')
#     print('3. change_json')
#     print('4. look_up_json')
#     print('5. Exit')
#     print('--------------')
#     choice = int(input('Enter action: '))
#     if choice == 0: break
#     elif choice == 1: add_json()
#     elif choice == 2: del_json()
#     elif choice == 3: change_json()
#     elif choice == 4: look_up()
#     elif choice == 5:
#         break
#     else: print('Error')


# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.

def create_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    print(script_dir)
    return os.path.join(script_dir, file_name)

def serialize_json(file_name, data):
    path = create_path(file_name)
    with open(path, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def deserialize_json(file_name):
    path = create_path(file_name)
    with open(path, 'r') as file:
        data = json.load(file)
    return data

try:
    file_name = 'employee.json'
    employees = {
        "Employees": [
            {
                "FirstName": "Denys",
                "LastName": "Zmiienko",
                "Age": "42"
            },
            {
                "FirstName": "Alex",
                "LastName": "Naumov",
                "Age": "41"
            }
        ]
    }
    serialize_json(file_name, employees)
    deserialized_employee = deserialize_json(file_name)
    print(deserialized_employee)
except Exception as e:
    print(e)


from pprint import pprint
def look_up():
    print("Company employees:")
    data = json.load(open("employee.json"))
    pprint(data)

def add_json():
    print("Adding Data to the Dictionary")
    data = json.load(open("employee.json"))
    FirstName = input("FirstName: ")
    LastName = input("LastName: ")
    Age = input("Age: ")
    new_data_base = [
        {
            "FirstName": FirstName,
            "LastName": LastName,
            "Age": Age
        },
    ]
    if FirstName not in data:
        data[FirstName] = new_data_base
    else:
        print('This country already exists.')
    with open("employee.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("Data added to dictionary")

def del_json():
    print("Removing data from a dictionary")
    data = json.load(open("employee.json"))
    LasttName = input("LasttName: ")
    if LasttName in data:
        del data[LasttName]
    else:
        print('Not find.')
    with open("employee.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("Data copied from dictionary")


def change_json():
    print("Changing Dictionary Data")
    data = json.load(open("employee.json"))
    LastName = input("LastName: ")
    if LastName in data:
        FirstName = input("FirstName: ")
        LastName = input("LastName: ")
        Age = input("Age: ")
        new_data_base = [
            {
                "FirstName": FirstName,
                "LastName": LastName,
                "Age": Age
            },
            ]
        data[LastName] = new_data_base
    else:
        print('Not find.')
    with open("employee.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("Data replaced in dictionary")


def filter_json_age():
    data = json.load(open("employee.json"))
    a = int(input("Enter age"))
    res = list(filter(lambda x: int(x['Age']) == a, data))
    print(res)

filter_json_age()

def filter_json_letter():
    data = json.load(open("employee.json"))
    l = input("Enter letter")
    res = list(filter(lambda x: x['LastName'] == l, data))
    print(res)

def auto_save_jeson():
    data = json.load(open("employee.json"))
    with open("employee.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

while True:
    print('Data_Base')
    print('--------------')
    print('1. add_json')
    print('2. del_json')
    print('3. change_json')
    print('4. look_up_json')
    print('5. filter_json_letter')
    print('6. filter_json_age')
    print('7. Exit')
    print('--------------')
    choice = int(input('Enter action: '))
    if choice == 0: break
    elif choice == 1: add_json()
    elif choice == 2: del_json()
    elif choice == 3: change_json()
    elif choice == 4: look_up()
    elif choice == 5: filter_json_age()
    elif choice == 6: filter_json_letter()
    elif choice == 7:
        data = json.load(open("employee.json"))
        with open("employee.json", "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        break
    else: print('Error')