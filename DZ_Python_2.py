# Задание 1
# Пользователь вводит с клавиатуры номер дня недели(1-7). Необходимо вывести на экран названия дня недели.
# Например, если 1, то на экране надпись понедельник,2 — вторник и т.д.

dayWeek = int(input("Enter day week 1-7"))
if dayWeek > 0 and dayWeek < 8:
    if dayWeek == 1:
        print("Sunday")
    elif dayWeek == 2:
        print("Monday")
    elif dayWeek == 3:
        print("Tuesday")
    elif dayWeek == 4:
        print("Wednesday")
    elif dayWeek == 5:
        print("Thursday")
    elif dayWeek == 6:
        print("Friday")
    elif dayWeek == 7:
        print("Saturday")
else:
    print("Error input")

# Задание 2
# Пользователь вводит с клавиатуры номер месяца (1-12). Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2 — февраль и т.д.

month = int(input("Enter month 1-12"))
if month > 0 and month < 13:
    if month == 1:
        print("January")
    elif month == 2:
        print("February")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("June")
    elif month == 7:
        print("July")
    elif month == 8:
        print("August")
    elif month == 9:
        print("September")
    elif month == 10:
        print("October")
    elif month == 11:
        print("November")
    elif month == 12:
        print("December")
else:
    print("Error input")

# Задание 3
# Пользователь вводит с клавиатуры число. Если число больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю «Number is equal to zero»

number = int(input("Enter number"))
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is equal to zero")

# Задание 4
# Пользователь вводит с клавиатуры целое шестизначное число. Написать программу, которая определяет,
# является ли введенное число — счастливым (Счастливым считается шестизначное число, у которого сумма
# первых 3 цифр равна сумме вторых трех цифр).
# Например, 123321 — счастливое число, так как 1+2+3 = 3+2+1.
# С другой стороны 378423 несчастливое число, так как 3+7+8 != 4+2+3.
# Если пользователь ввел не шестизначное число требуется вывести сообщение об ошибке.

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

# Задание 5
# Пользователь вводит шестизначное число. Необходимо поменять в этом числе первую и шестую цифры, а также
# вторую и пятую цифры. Например, 723895 должно превратиться в 593827.
# Если пользователь ввел не шестизначное число требуется вывести сообщение об ошибке

numberChange = int(input("In a six-digit number, swap the first and sixth digits, as well as the second and fifth digits. Enter the number: "))
didgit_1 = int(numberChange / 100000)
didgit_2 = int((numberChange / 10000) % 10)
didgit_3 = int((numberChange / 1000) % 10)
didgit_4 = int((numberChange / 100) % 10)
didgit_5 = int((numberChange / 10) % 10)
didgit_6 = int(numberChange % 10)
if numberChange >= 99999:
    print(didgit_6, didgit_5, didgit_3, didgit_4, didgit_2, didgit_1)
else:
    print("Number is not six-digit")

# Задание 6
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# 1000 — 8%. Пользователь вводит с клавиатуры уровень продаж для трех менеджеров.
# Определить их зарплату,определить лучшего менеджера, начислить ему премию 200$, вывести итоги на экран.

manager1 = int(input("Enter sales manager 1: "))
manager2 = int(input("Enter sales manager 2: "))
manager3 = int(input("Enter sales manager 3: "))
salery = 200
if manager1 > 1000:
    wage1 = salery + manager1 * 0.08
else:
   if manager1 < 1000 and manager1 >= 500:
       wage1 = salery + manager1 * 0.05
   else:
       wage1 = salery + manager1 * 0.03
if manager2 > 1000:
    wage2 = salery + manager2 * 0.08
else:
   if manager2 < 1000 and manager2 >= 500:
       wage2 = salery + manager2 * 0.05
   else:
       wage2 = salery + manager2 * 0.03
if manager3 > 1000:
    wage3 = salery + manager3 * 0.08
else:
   if manager3 < 1000 and manager3 >= 500:
       wage3 = salery + manager3 * 0.05
   else:
       wage3 = salery + manager3 * 0.03
if wage1 > wage2 and wage1 > wage3:
   print("Best of the best manager 1")
   wage1 += 200
if wage2 > wage1 and wage2 > wage3:
   print("Best of the best manager 2")
   wage2 += 200
if wage3 > wage1 and wage3 > wage2:
   print("Best of the best manager 2")
   wage3 +=200
print("Sales manager 1: ",wage1)
print("Sales manager 2: ",wage2)
print("Sales manager 3: ",wage3)

# Дополнительно
#  Грузовой самолет должен пролететь с грузом из пункта А в пункт С через пункт В.
# Емкость бака для топлива у самолета – 300литров. Потребление топлива на 1 км в зависимости
# от веса груза у самолета следующее:
# - до 500 кг: 1 литров / км
# - до 1000 кг: 4 литров / км
# - до 1500 кг: 7 литров / км
# - до 2000 кг: 9 литров / км.
# - более 2000 кг – самолет не поднимает.
# Пользователь вводит расстояние между пунктами А и В, и расстояние между пунктами В и С, а
# также вес груза. Программа должна рассчитать какое минимальное количество топлива
# необходимо для дозаправки самолету в пункте В, чтобы долететь из пункта А в пункт С. В
# случае невозможности преодолеть любое из расстояний – программа должна вывести
# сообщение о невозможности полета по введенному маршруту.

distans_AB = int(input("Enter distans between A and B: "))
distans_BC = int(input("Enter distans between B and C: "))
weight = int(input("Enter weight cargo: "))
fuel_AB = 0
fuel_BC = 0
fuel = 0

if weight <= 500:
    fuel_AB = distans_AB
    fuel_BC = distans_BC

elif weight <= 1000:
    fuel_AB = distans_AB * 4
    fuel_BC = distans_BC * 4

elif weight <= 1500:
    fuel_AB = distans_AB * 7
    fuel_BC = distans_BC * 7

elif weight <= 2000:
    fuel_AB = distans_AB * 9
    fuel_BC = distans_BC * 9

else:
    print("The plane does not lift more than 2000 kg.")

fuel = fuel_AB + fuel_BC

if fuel_AB >= 300 or fuel_BC >= 300:
    print("Impossible to cover any of the distances.")

else:
    print("Minimum fuel needed: ")
    print("Fuel needed for A_B: ",  fuel_AB)
    print("Fuel needed for B_C: ",  fuel_BC)