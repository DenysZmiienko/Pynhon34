# Задание 1
# Напишите программу, которая принимает строку и применяет лямбда-выражение для манипуляций с текстом,
#  например, для удаления определенных символов.

str = input('Enter string: ')
print(str)
new_str = ''.join(list(filter(lambda c: c!='/', str)))
print(new_str)

# Задание 2
# Создайте список чисел и используйте лямбда-выражение для вычисления суммы,
# среднего значения или других агрегированных статистических данных для этого списка.

myNumbers = [1, 2, 3, 4, 5]
sum = (lambda x: sum(x))(myNumbers)
print(sum)

from functools import reduce
sum = reduce((lambda x, y: x + y), myNumbers)
print(sum)

average = reduce(lambda x, y: x + y, myNumbers) / len(myNumbers)
print(average)

# Задание 3
# Напишите функцию, которая получает два списка в
# качестве параметра и возвращает список, содержащий элементы обоих списков.

from functools import reduce
list = [['a', 'b', 'c', 'd'],['i', 'f', 'j', 'h']]
print(list)
result_list = reduce(lambda x, y: x + y, list)
print(result_list)

list1 = ['a', 'b', 'c', 'd']
list2 = ['i', 'f', 'j', 'h']
result_list_2 = list(map(lambda x, y: x+y, list1, list2))
print(result_list_2)

# Задание 4
# Написать рекурсивную функцию нахождения наибольшего общего делителя двух целых чисел.

def greatest_common_divisor(a, b):
    if (b == 0):
        return a
    else:
        return greatest_common_divisor(b, a % b)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
GCD = greatest_common_divisor(a, b)
print('Greatest common divisor: ')
print(GCD)

# Задание 5
# Создайте калькулятор, используя lambda-функции для каждой арифметической операции (сложение, вычитание, умножение, деление).
#  Протестируйте калькулятор с разными парами чисел и операторами.

while True:
    first = int(input('Enret first number:'))
    second = int(input('Enret second number:'))
    operation = input('Enret type operation (+,-,/,*,**):')
    if operation == '+':
        result = lambda x, y: x + y
        print(result(first, second))
    elif operation == '-':
        result = lambda x, y: x - y
        print(result(first, second))
    elif operation == '*':
        result = lambda x, y: x * y
        print(result(first, second))
    elif operation == '/':
        result = lambda x, y: x / y
        print(result(first, second))
    elif operation == '**':
        result = lambda x, y: x ** y
        print(result(first, second))
    else:
        print("Error: incorrect input")
    enter_again = input("Enter again? (Y/N): ")
    if enter_again != "Y":
        break

# Задание 6
# Создайте генератор паролей с использованием lambda-функций.
# Используйте lambda-функции для генерации случайных символов и создайте пароль,
# состоящий из заданного количества символов.

import string
import random

def check_password(password):
    res_dict = [
    lambda password: (x.isupper() for x in password),
    lambda password: (x.islower() for x in password),
    lambda password: (x.isdigit() for x in password),
    lambda password: (x in '!@#$%^&*()-+' for x in password)]
    result = [x for x in [i(password) for i in res_dict] if x != True]


lenght_pass = int(input('Enter lenght password'))
print(((''.join(random.sample(string.ascii_letters + string.punctuation, lenght_pass)))))

# Задание 7
# Создайте lambda-функцию, которая принимает строку и возвращает её в верхнем регистре,
# если она содержит более 5 символов,
# и в нижнем регистре в противном случае. Протестируйте функцию на различных строках.

data = input('Enter string')
if len(data) > 5:
    new_len = lambda a: a.upper()
    print(new_len(data))
elif len(data) < 5:
    new_len = lambda a: a.lower()
    print(new_len(data))
else:
    print("Error: incorrect input")
