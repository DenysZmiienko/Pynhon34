# Задание 1
# В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
# По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
# Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.
# Пример экрана вывода:
# >>> Введите расстояние которое пробежал спортсмен в первый день: 10
# >>> Введите расстояние которое должен пробежать спортсмен: 20
# Расстояние в 20 км спортсмен пробежит за 9 дней
# >>> Введите расстояние которое пробежал спортсмен в первый день: 10
# >>> Введите расстояние которое должен пробежать спортсмен: 100
# Расстояние в 20 км спортсмен пробежит за 26 дней

start = int(input("Enter the distance the athlete ran on the first day: "))
finish = int(input("Enter the distance the athlete must run: "))
day = 1
while finish - start > 0:
    start *= 1.1
    day += 1
print(f'An athlete will run a distance of {finish} km in {day} days')

# Задание 2
# Реализуйте игру Камень,ножницы,бумага. По примеру как мы делали игру Угадай число.
# Игра длится три раунда, после чего выводится победитель и предлагается сыграть еще раз.
# Человек вводит строку R or P or S (R- rock, P - paper, S - scissors).
# Выбор компьютера реализовать с использование рендома. (random.choice(“r”,”p”,”s”))
# Предусмотреть проверку ввода некорректных символов, так же минимальный пользовательский интерфейс.

import random
print("Let's play the game Rock - Paper - Scissors")
while True:
    user_action = input("Make a choice — Rock - Paper - Scissors: ")
    possible_actions = ["Rock", "Paper ", "Scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou choosed {user_action}, the computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"You and computer chose {user_action}. Draw")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("You chose the Rock, the computer chose the Scissors. The Scissors have become dull. You Win.")
        else:
            print("You chose the Rock, the computer chose the Paper. The Paper covered the Rock. You lose.")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("You chose the Paper, the computer chose the Rock. The Paper covered the Rock. You Win.")
        else:
            print("You chose the Paper, the computer chose the Scissors. Scissors cutting Paper. You lose.")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("You chose the Scissors, the computer chose the Paper. Scissors cutting Paper. You Win.")
        else:
            print("You chose the Scissors, the computer chose the Rock. The Scissors have become dull. You lose.")
    else:
        print("Error: incorrect input")
    play_again = input("Play again? (Y/N): ")
    if play_again != "Y":
        break

        # Задание 3
# Пользователь вводит число. Определить количество цифр в этом числе, посчитать их сумму и среднее арифметическое.
# Определить количество нулей в этом числе. Общение с пользователем организовать через меню.

inputn = int(input("Enter number:"))
n = inputn
total = 0
product = 1
count = 0
countZero = 0
while inputn:
    total += inputn % 10
    product *= inputn % 10
    count += 1
    inputn //= 10
    if inputn == 0:
        countZero += 1
print('Number of digits: ', count)
print('Sum number: ', total)
print('Arithmetic average: ', total / count)
print('Zero: ', countZero)
choice = input("1 - Number of digits, 2 - Sum number, 3 - Arithmetic average, 4 - Zero ")
while choice > 0 and choice < 5:
    if choice == 1:
         print('Number of digits: ', count)
    elif choice == 2:
        print('Sum number: ', total)
    elif choice == 3:
        print('Arithmetic average: ', total/count)
    elif choice == 4:
        print('Zero: ', countZero)
    else:
        print('error')