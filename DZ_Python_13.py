# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли # их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.

f = open('text.txt', 'r', encoding='utf-8')
lines1 = set(f.read().split())
f.close()
f = open('text2.txt', 'r', encoding='utf-8')
lines2 = set(f.read().split())
f.close()
print("The first set: ", lines1)
print("The second set: ", lines2)
print("Intersection of sets: ", lines1.intersection(lines2))

# Задание 2
# Дан текстовый файл. Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:
# Количество символов;
# Количество строк;
# Количество цифр.

with open('text.txt') as f:
	txt = f.read()
	print(txt)
	print(sum(map(str.isalpha, txt)), 'letters')
	print(len(txt.split()), 'words')
	print(txt.count('\n') + 1, 'lines')
	print(len([i for i in txt if i.isdigit()]), 'numbers')

# Задание 3
# Дан текстовый файл. Удалить из него последнюю
# строку. Результат записать в другой файл.

f_read = open('text3.txt', 'r', encoding='utf-8')
f_write = open('text4.txt', 'w', encoding='utf-8')
f1 = f_read.readlines()
f2 = f1[:-1]
for line in f2:
	f_write.write(line)
print("Source document: ", f1)
print("Modified document: ", f2)
f_read.close()
f_write.close()

# Задание 4
# Дан текстовый файл. Найти длину самой длинной строки.

with open('text5.txt', 'r', encoding='utf-8') as f:
    print(max(f, key=len))

# Задача 5: Создать программу для записи и чтения текстовых записей в файле, создавая эффективную систему управления дневником.
#
# Инструкции:
#
# Создайте меню с возможностью добавления новой записи в дневник и просмотра всех записей.
# Реализуйте функцию добавить_запись(дневник, запись), которая будет добавлять новую запись (строку текста)
# в файл "дневник.txt". Если файл не существует, программа должна создать его.
# Реализуйте функцию просмотреть_записи(дневник), которая будет читать и выводить на экран все записи из файла
# "дневник.txt". Если файла нет или в нем нет записей, программа должна выводить соответствующее сообщение.
# При запуске программы, предоставьте пользователю возможность выбирать действия (добавить запись, просмотреть записи,
# выйти из программы) до тех пор, пока он не решит выйти.
# При добавлении записи, программа должна предложить ввести текст записи, добавить дату и время создания записи автоматически.
# При просмотре записей, программа должна выводить записи в формате:
#
# Дата и время создания записи:
# Текст записи
# -----------------------
# Каждая запись должна отделяться пунктирной линией.
# Убедитесь, что записи сохраняются в файле между запусками программы и не заменяются при каждом новом добавлении.
# Реализуйте обработку ошибок, например, если файл "дневник.txt" не может быть прочитан или записан.

import os
from datetime import datetime

ADD = 1
SHOW = 2
EXIT = 3

def main():
    choice = 0
    while choice != EXIT:
        choice = get_menu_choice()
        if choice == ADD:
            add()
        elif choice == SHOW:
            show()

def get_menu_choice():
    print()
    print('Diary')
    print('------------------------')
    print('1. Search for information')
    print('2. Add information')
    print('3. Exit')
    print('------------------------')
    choice = int(input('Enter action: '))
    while choice < ADD or choice > EXIT:
        choice = int(input('Enter action: '))
    return choice

def add():
    another = 'y'
    diary_file = open('diary.txt', 'a', encoding='utf-8')
    while another == 'y' or another == 'Y':
        print('------------------------------------------------------------------------------------------------')
        print('Enter the following information in your diary:')
        mtime = os.path.getmtime(diary_file)
        descr = input('Enter item name or description: ')
        qty = int(input('Give a grade for the subject (from 1 to 12 points): '))
        diary_file.write(f'{mtime} ')
        diary_file.write(f'{descr} ')
        diary_file.write(f'{qty} ')
        print('------------------------------------------------------------------------------------------------')
        print('Would you like to add another entry?')
        another = input('Y yes, everything else = no:')
    diary_file.close()
    print('Data added to diary. txt ')

def show():
    diary_file = open('diary.txt', 'r', encoding='utf-8')
    descr = diary_file.readline()
    while descr != '':
        stat = os.stat(diary_file)
        ctime = stat.st_ctime
        ctime_readable = datetime.fromtimestamp(ctime)
        qty = int(diary_file.readline())
        print(f'Date: {ctime_readable} ')
        print(f'Enter item name: {descr} ')
        print(f'Points: {qty} ')
        descr = diary_file.readline()
    diary_file.close()

main()