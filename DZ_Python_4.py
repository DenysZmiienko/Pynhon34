# Задание 1
# Напишите программу, которая генерирует случайное число от 1 до 100.
# Запросите пользователя угадать это число. Используйте блок try-
# чтобы обработать ошибки ввода (например, если пользователь вводит не число).
# Выводите подсказки, является ли загаданное число больше или меньше введенного пользователем.
# Повторяйте цикл, пока пользователь не угадает число.

import random
try:
    num = random.randint(1,100)
    user_num = int(input("Guess the number from 1 to 100"))
    while num != user_num:
        if num > user_num:
            print("Your number is less than what the computer intended")
        elif num < user_num:
            print("Your number is higher than the computer intended")
        user_num = int(input("uess the number from 1 to 100"))
except (ValueError, ZeroDivisionError, TypeError):
    print("Error")
else: print("Winer")
print(num)
print(user_num)

# Задание 2
# Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.

try:
    number = int(input("Enter any integer number "))
    new_number = 0
    i = 0
    while number > 0:
        num = number % 10
        if num != 3 and num != 6:
            new_number = new_number + num * 10 ** i
            i = i + 1
        number = number // 10
    print("New number:", new_number)
except (ValueError, ZeroDivisionError, TypeError):
    print("Error")

# Задание 3
# Пользователь вводит с клавиатуры размер стороны
# квадрата. Требуется отобразить на экран незаполненный квадрат (отображаются только границы квадрата).
# Размер стороны равен введённому размеру.

try:
    size = int(input("Enter size square"))
    for i in range(size):
        for j in range(size):
            if i == 0 or j == 0 or i == size-1 or j == size-1:
                print("*",end="")
            else:
                print(" ",end="")
        print("")
except (ValueError, ZeroDivisionError, TypeError):
    print("Error")

# Задание 4
# Пользователь вводит с клавиатуры длину и ширину
# прямоугольника. Требуется отобразить на экран незаполненный прямоугольник (отображаются только границы прямоугольника).
# Размер длины и ширины равен введенным данным.

try:
    length = int(input("Enter size length"))
    width = int(input("Enter size width"))
    for i in range(length):
        for j in range(width):
            if i == 0 or j == 0 or i == length-1 or j == width-1:
                print("*",end="")
            else:
                print(" ",end="")
        print("")
except (ValueError, ZeroDivisionError, TypeError):
    print("Error")

