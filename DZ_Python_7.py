# Задание 1
# Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
# Функция принимает в качестве параметра: длину линии,направление, символ.

def draw(length, direction, symbol):
    if direction == 'horizontally':
        for i in range(length):
            print(symbol, end="")
    elif direction == 'vertically':
        line = ""
        for i in range(length):
            line += symbol
            print(line)


draw(20, 'horizontally', "!")

# Задание 2
# Напишите функцию, которая возвращает максимальное из четырёх чисел. Числа передаются в качестве
# параметров.

def max_four(num1, num2, num3, num4):
    if num1 > num2:
        if num1 > num3:
            print(max(num1, num4))
        else:
            print(max(num3, num4))
    else:
        if num2 > num3:
            print(max(num2, num4))
        else:
            print(max(num3, num4))

max_four(125,4,10,0)

# Задание 3
# Написать функцию, которая получает в качестве параметров 2 целых числа и возвращает сумму чисел из диапазона между ними.

def sum_numbers(num5, num6):
    if num5 == num6:
        print(num5)
    elif num5 > num6:
        num5, num6 = num6, num5
    print(sum(range(num5, num6 + 1)))

sum_numbers(8, 7)

# Задание 4
# Написать функцию, определяющую количество положительных, отрицательных и нулевых элементов передаваемого ей массива.

from random import random
def count_numbers():
    pozitiv = 0
    negativ = 0
    zero = 0
    list_num = []
    for i in range(30):
        number = int((random() * 25) - 10)
        list_num.append(number)
        print(number, end=', ')
        if number > 0:
            pozitiv += 1
        elif number < 0:
            negativ += 1
        else:
            zero += 1
    print()
    print("Pozitiv numbers: ", pozitiv)
    print("Negativ numbers: ", negativ)
    print("Zero: ", zero)

count_numbers()

# Задание 5
# Написать функцию, которая определяет, является ли «счастливым» шестизначное число.

def luky():
    numberLucky = int(input("Is a six-digit number lucky? Enter the number and check: "))
    didgit_1 = int(numberLucky / 100000)
    didgit_2 = int((numberLucky / 10000) % 10)
    didgit_3 = int((numberLucky / 1000) % 10)
    didgit_4 = int((numberLucky / 100) % 10)
    didgit_5 = int((numberLucky / 10) % 10)
    didgit_6 = int(numberLucky % 10)
    if numberLucky >= 99999:
        if (didgit_1 + didgit_2 + didgit_3) == (didgit_4 + didgit_5 + didgit_6):
            print("Number is lucky")
        elif (didgit_1 + didgit_2 + didgit_3) != (didgit_4 + didgit_5 + didgit_6):
            print("Number is not lucky")
    else:
        print("Number is not six-digit")

luky()

# Задание 6
# Напишите две функции: одну для перевода температуры из Цельсия в Фаренгейт (celsius_to_fahrenheit) и другую для обратного перевода (fahrenheit_to_celsius).
# Протестируйте обе функции, переведя несколько температурных значений.
#
def main():

    celsius = int(input('Enter temperatury in celsius: '))
    celsius_to_fahrenheit(celsius)

    fahrenheit = int(input('Enter temperatury in farengeyt: '))
    fahrenheit_to_celsius(fahrenheit)

def celsius_to_fahrenheit(temperaturaCel):
    result_F = temperaturaCel * 1.8 + 32
    print(f'{temperaturaCel} celsius - this is {result_F} farengeyt.')

def fahrenheit_to_celsius(temperaturaFar):
    result_C = (temperaturaFar - 32) / 1.8
    print(f'{temperaturaFar} farengeyt - this is {result_C} celsius.')

main ()

# Задание 7
# Напишите программу-симулятор банковского счета с использованием функций. Реализуйте функции для внесения и снятия денег,
# проверки баланса, а также функцию для подсчета процентов по вкладу. Дайте пользователю возможность выбора операции
# и взаимодействия с программой.

def main():
    deposit_of_money = get_deposit_of_money()
    withdrawal_of_money = get_withdrawal_of_money()
    percentage_calculation = percentage(deposit_of_money)
    balans = deposit_of_money + (deposit_of_money * percentage_calculation) - withdrawal_of_money
    print(f' Your balance is ${balans} grn. ')
    if balans < 0:
        print('You owe money to the bank')
    choice = int(input('ВEnter options: '))

def get_deposit_of_money():
    deposit_of_money = float(input('What amount to put on the account? '))
    return deposit_of_money

def get_withdrawal_of_money():
    withdrawal_of_money = float(input('What amount to withdraw from the account? '))
    return withdrawal_of_money

def percentage(deposit_of_money):
    if deposit_of_money < 10000.00:
        rate = 0.10
    elif deposit_of_money >= 10000 and deposit_of_money <= 14999.99:
        rate = 0.11
    elif deposit_of_money >= 15000 and deposit_of_money <= 17999.99:
        rate = 0.12
    elif deposit_of_money >= 18000 and deposit_of_money <= 21999.99:
        rate = 0.13
    else:
        rate = 0.14
    return rate

def display_menu():
    print(' Menu')
    print( '1. deposit_of_money')
    print( '2. withdrawal_of_money' )
    print( '3. percentage_calculation')
    print( '4. balance')
    print('5. quit')

deposit_of_money = 1
withdrawal_of_money = 2
percentage_calculation = 3
balans = 4
quit = 5
choice = 0
while choice != 5:
    display_menu()
    choice = int(input('Enter options: '))
    if choice == 1:
        get_deposit_of_money()
    elif choice == 2:
        get_withdrawal_of_money()
    elif choice == 3:
        percentage(deposit_of_money)
    elif choice == 4:
        main()
    elif choice == 5:
        print('Quit')
    else:
        print('Error')

# Задание 8
# Напишите программу-генератор паролей с использованием функций. Реализуйте функцию, которая генерирует случайный пароль
# заданной длины, а также функцию для установки пользовательских настроек, таких как использование заглавных букв,
# цифр и специальных символов. Дайте пользователю возможность выбора параметров генерации пароля.

def main():
    import string
    import random

    def generate_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def password_check(password):
        check = True
        checkDigit = 0
        checkLower = 0
        checkUpper = 0
        checkPunkt = 0
        for s in password:
            if s.isdigit():
                checkDigit = True
            elif s.islower():
                checkLower = True
            elif s.isupper():
                checkUpper = True
            elif s in string.punctuation:
                checkPunkt = True
        if checkDigit and checkUpper and checkLower and checkPunkt:
            print("Password is OK")
        else:
            print("Password is bad")

    password_length = int(input("Enterr lenght password: "))
    generated_password = generate_password(password_length)
    print("Your password:", generated_password)
    password_check(generated_password)
main()