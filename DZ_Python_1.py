# Задание 1
# Приведите к целому типу число 2.99

a = 2.99
print(int(a))

# Задание 2
# Написать программу, которая обеспечивает ввод с клавиатуры переменной kol целого типа.

kol = int(input("Enter integer variable kol: "))
print(kol)

# Задание 3
# Написать программу, обеспечивающую ввод с клавиатуры значения переменной radius типа float.

radius = float(input("Enter variable float radius: "))
print(radius)

# Задание 4
# Напишите программу в которой вычисляется площадь окружности по ее радиусу
# Пример вывода программы : r = 1.1 Area = 3.8013271108436504

r = float(input("Enyer radius: "))
Area = 0
print('r=',r, 'Area =', (3.14 * r ** 2))

# Задание 5.
# Пользователь вводит с клавиатуры расстояние до аэропорта и время, за которое нужно доехать. Вычислить скорость, с которой ему нужно ехать.

distancePoints = float(input("Enter distance points: "))
departureTimes = float(input("Enter departure times: "))
speed = 0
print("Speed = ", distancePoints / departureTimes)

# Задание 6.
#  Пользователь вводит с клавиатуры время начала и время завершения телефонного разговора (часы, минуты и секунды). Посчитать стоимость разговора,
#  если стоимость минуты – 30 копеек.

hour_begin = int(input("Enter hour begin; "))
min_begin = int(input("Enter minutes begin; "))
sec_begin = int(input("Enter seconds begin; "))
hour_end = int(input("Enter hour end; "))
min_end = int(input("Enter minutes end; "))
sec_end = int(input("Enter seconds end; "))
tmp_hour = (hour_end - hour_begin) * 3600
tmp_min = (min_end - min_begin) * 60
tmp_sec = sec_end - sec_begin / 60
tmp_speak = 0
print("Cost speak : ", (tmp_hour + tmp_min + tmp_sec) * 0.3)

# Задание 7.
#  Пользователь вводит с клавиатуры расстояние, расход бензина на 100 км и стоимость трех видов бензина. Вывести на экран сравнительную таблицу
#  со стоимостью поездки на разных видах бензина.

distanceTrip = float(input("Enter distance trip: "))
disel = float(input("Enter distance trip disel: "))
gasolin = float(input("Enter distance trip gasolin: "))
gas = float(input("Enter distance trip gas: "))
cost_disel = float(input("Enter cost_disel: "))
cost_gasolin = float(input("Enter cost_gasolin: "))
cost_gas = float(input("Enter cost_gas: "))
var_disel = 0
var_gasolin = 0
var_dgas = 0
print("Comparison disel :", disel * distanceTrip / 100 * cost_disel)
print("Comparison gasoline :", gasolin * distanceTrip / 100 * cost_gasolin)
print("Comparison gas :", gas * distanceTrip / 100 * cost_gas)

# Задание 8.
#  Пользователь вводит с клавиатуры время в секундах, прошедшее с начала дня. Вывести на экран текущее время в часах, минутах и секундах.
# Посчитать, сколько часов, минут и секунд осталось до полуночи.

total_seconds = float(input("Enter the time in seconds elapsed since the beginning of the day :"))
hours = total_seconds // 3600
minutes = (total_seconds // 60) % 60
seconds = total_seconds % 60
print('Hours:', hours)
print('Minutes:', minutes)
print(' Seconds:', seconds)
end_seconds = 86400 - total_seconds
print("Seconds midnight left: ", (86400 - total_seconds))
end_hours = end_seconds // 3600
end_minutes = (end_seconds // 60) % 60
end_seconds = end_seconds % 60
print("It's midnight left: ")
print('Hours midnight:', end_hours)
print('Minutes midnight:', end_minutes)
print(' Seconds midnight:', end_seconds)

# Задание 9.
# Пользователь вводит с клавиатуры время в секундах, прошедшее с начала рабочего дня. Посчитать, сколько целых часов ему осталось сидеть на работе,
# если рабочий день – 8 часов. у которая позволяет переводить время вводимое пользователем с клавиатуры и представленное в секундах в вермя представленное в часах,
# минутах и секундах.

time_sec_work = float(input("Enter the time in seconds since the start of the working day :"))
end_time_work = 28880 - time_sec_work
print("Hours left to sit at work: ", (end_time_work // 3600))
print("Minutes left to sit at work: ", (end_time_work // 60) % 60)
print("Seconds left to sit at work: ", (end_time_work % 60))