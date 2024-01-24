# Задание 1
# Дан список чисел, отфильтровать только положительные

numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
even_numbers = list(filter(lambda x: x > 0, numbers))
print(numbers)
print(even_numbers)

# Задание 2
# Дан список чисел, отфильтровать числа в диапазоне указанным пользователем

numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
a = int(input("Enter the start of the range"))
b = int(input("Enter the finished of the range"))
number_range = list(filter(lambda x: (x[a:b]), numbers))
print(number_range)

# Задание 3
# Дан список чисел, отфильтровать все целочисленные значения

numList = [1, 2.0, 3.1, 4, 5, 6, 7.9]
integer_values = filter(lambda x: type(x) is int, numList)
print(list(integer_values))

# Задание 4
# Дан список логинов пользователей, добавьте каждому логину приставку "$"

userLogs = ['123user34', 'Userqwerty', 'user234dffdf', 'User-23', 'userADMIN']
print("Old login:", userLogs)
def modifyUserLogs(userLogs):
    return userLogs + '$'

newUserLogs = list(map(modifyUserLogs, userLogs))
print("New login:", newUserLogs)

# Задание 5
# На основе трех списков разных значений, сформировать список,
# елемент которого содержит набор из елементов других списков.

dataList = [('a', 1, '!'), ('b', 2, '?'), ('c', 3, '*'), ('d', 4, '+')]
x, y, z = zip(*dataList)
result = (list(x), list(y), list(z))
print(result)

# Задание 6
# Напишите программу, которая принимает список целых чисел и возвращает список строк, представляющих эти числа.

print('Enter numbers: ')
myList = [int(value) for value in input().split()]
print(myList)
print(" ".join(map(str, myList)))