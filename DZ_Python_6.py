Задание 1
Создайте список, представляющий собой баллы студентов за экзамен. Напишите программу, которая выводит средний балл, максимальный
и минимальный балл, а также количество студентов, получивших балл выше среднего.

import random
grade = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
score = random.choices(grade, k=20)
exam_score = score.copy()
print('Student exam scores: ', exam_score)
print('Minimum exam score: ', min(exam_score))
print('Maximum exam score: ', max(exam_score))
average = sum(exam_score) / len(exam_score)
print('Average exam score: ', average)
count = 0
for value in exam_score:
    if value > average:
        count +=1
print('Number of students who scored above average: ', count)

Задание 2
Пользователь с клавиатуры вводит элементы списка
целых и некоторое число. Необходимо посчитать сколько раз данное число присутствует в списке. Результат
вывести на экран.

test_scores = []
again = 'Y'
while again == 'Y':
    value = int(input('Enter element: '))
    test_scores.append(value)
    print('Enter next element?')
    again = input('Y = Yes, N = not: ')
    print(test_scores)
num = int(input('Enter number'))
print(f'This number appears in the list {test_scores.count(num)} times')

Задание 3
Создайте список слов. Напишите программу, которая запрашивает у пользователя слово и выводит сообщение о том, есть ли это слово в списке.
Если слово не найдено, предложите пользователю добавить его в список.

names = ['Bill', 'Govard', 'Leo', 'Jastin', 'Fill']
searched_name = input('Enter name: ')
if searched_name in names:
    print(f'{searched_name} search in list.')
else:
    print(f'{searched_name} not searched in list')
    names.append(searched_name)
    print('New list name: ', names)

# Задание 4 Доп*
# Написать имитацию кассового аппарата для магазина, торгующего
# новогодними товарами. Кассир должен выбрать товар из списка, ввести
# его количество, затем выбрать следующий товар. По завершению ввода
# вывести на экран всю сумму покупки. Предусмотреть наличие скидки. В
# списке товаров должно быть не меньше 4х товаров, должна отображаться
# их цена. Предусмотреть неправильно вводимые данные.
# • Реализовать возможность обслуживания нескольких клиентов подряд
# • Хранение общей выручки магазина
# • Ограничить количество товара в магазине.

# from datetime import datetime
# datta = datetime.now()
# print("Магазин Шестёрочка. Кассовый аппарат №01")
# print("Введите код товаров и их количество:\n"
#       "сахар   - 001\n"
#       "яйца    - 002\n"
#       "молоко  - 003\n"
#       "йогурт  - 004\n"
#       "сыр     - 005\n"
#       "колбаса - 006\n")
# s1, s2, s3, s4, s5, s6 = 60, 65, 50, 35, 600, 500
# k1 = k2 = k3 = k4 = k5 = k6 = 0
# n1 = "сахар"
# n2 = "яйца"
# n3 = "молоко"
# n4 = "йогурт"
# n5 = "сыр"
# n6 = "колбаса"
# a = "000"
# b = 1
# while a != "" and b != 0:
#     a = input()
#     b = input()
#     if a == "001":
#         k1 = s1 * float(b)
#     if a == "002":
#         k2 = s2 * float(b)
#     if a == "003":
#         k3 = s3 * float(b)
#     if a == "004":
#         k4 = s4 * float(b)
#     if a == "005":
#         k5 = s5 * float(b)
#     if a == "006":
#         k6 = s6 * float(b)
# summ = k1 + k2 + k3 + k4 + k5 + k6
# summ2 = 0
# print("Карта покупателя(если отсутствует, нажмите Enter):")
# if input() != "":
#     summ2 = summ * 0.95
# else:
#     summ2 = summ
# if a == "001":
#     print("Магазин Шестёрочка\n"
#           "Чек\n"
#           "Дата", datta, "\n", n1, b, k1, "\n", "Итого:", summ2)





product = {'торт': [['сгущенное молоко', 'пшеничная мука', 'куриные яйца', 'сода пищевая', 'уксус',
                     'пшеничная мука', 'сахар', 'молоко', 'сливочное масло'], 10, 300],
           'пирожное': [['печенье', 'сгущенное молоко', 'сливочное масло', 'какао-порошок'], 5, 1500],
           'маффин': [['яйцо куриное', 'молоко', 'мука пшеничная', 'сахар', 'масло растительное', 'разрыхлитель',
                       'какао', 'соль'], 6, 700]
           }
while True:
    choice = input('1 - название – описание, 2 - название – цена, 3 - название – количество, 4 - Вся информация, '
                   '5 - Приступить к покупке: ')
    if choice == '1':
        for key, value in product.items():
            print(key, '-', ', '.join(value[0]))
    if choice == '2':
        for key, value in product.items():
            print(key, f'- цена: {value[1]} руб за 100гр.')
    if choice == '3':
        for key, value in product.items():
            print(key, f'- кол-во: {value[2]} гр.')
    if choice == '4':
        for key, value in product.items():
            print(f'\n {key}', '\nСостав:', ", ".join(value[0]), f'\nЦена: {value[1]} руб за 100 гр.',
                  f'\nКоличество: {value[2]} гр.')
    else:
        cost = 0
        while True:
            name_product = input("Введите названия продукта: (торт, пирожное, маффин)\n "
                                 " или введите n – выход из программы: ")
            if name_product == 'n' or name_product not in product:
                break
            gram = float(input('Сколько грамм вы хотите купить? '))
            if gram > product[name_product][2]:
                print('У нас столько нет, выберите другое кол-во или товар')
                continue
            print(cost)
            cost = cost + (gram / 100 * product[name_product][1])
            product[name_product][2] -= gram
        print(f'Вам надо заплатить {cost} руб ')
    for key, value in product.items():
        print('Остатки: ', key, value[2], 'гр')
    print('До свидания.')