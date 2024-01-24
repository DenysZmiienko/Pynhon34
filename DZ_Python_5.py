# 1 Напишите программу на Python, которая:
# Запрашивает у пользователя ввод строки.
# Выводит длину введенной строки.
# Переводит строку в верхний и нижний регистр.
# Выводит первые 3 символа строки.
# Проверяет, начинается ли строка с определенного префикса, введенного пользователем.
# Заменяет все пробелы в строке на подчеркивания.
# Проверяет, состоит ли строка только из букв.

str = input('Enter string: ')
print('Length of the entered string: ', len(str))
print('Uppercase string: ', str.upper())
print('Lowercase string: ', str.lower())
print('First 3 characters of line: ', str[0:3])
print('Whether the line starts with a certain prefix? ')
prefix = input('Enter prefix: ')
print('The line starts with a certain prefix: ', str.startswith(prefix))
print('Replace all spaces in the line with underscores: ', str.replace(" ", "_"))
print('The string consists only of letters: ', str.isalpha())

# 2. Задание: Работа с форматированием строк
# Напишите программу, которая:
# Запрашивает у пользователя ввод имени и возраста.
# Использует строки для вывода приветствия с использованием введенных данных.
# Создает строку, представляющую собой информацию о пользователе в формате "Имя: [имя], Возраст: [возраст]".
# Выводит отформатированный текст, представляющий информацию о пользователе.

name = input('What is your name ')
age = input('How old are you?: ')
message = "My name is {0} and I am {1} years old.".format(name, age)
print(message)

# 3. Задание: Работа с подстроками и методами строк
# Напишите программу, которая:
# Запрашивает у пользователя ввод строки.
# Использует методы строк для определения, содержит ли строка подстроку "Python".
# Находит индекс первого вхождения символа "o" в строке.
# Использует срезы для извлечения слова между вторым и пятнадцатым символами включительно.
# Переворачивает строку в обратном порядке и выводит результат.

str1 = input('Enter string: ')
print('Does the string contain the substring "Python"? ', str1.startswith('Python'))
print('Occurrence of the first "o" character in a string: ', str1.index('o'))
print('Slices for extracting the word between the second and fifteenth characters inclusively: ', str1[2:15])
print('Revers string: ', str1[::-1])

# Задание 4
# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на экран измененный текст.

text = input("Enter text: ")
reserved_words = input("Enter reserved words: ").split()
for word in reserved_words:
   text = text.replace(word, word.upper())
print("Changed text: ", text)

# Задание 5
# Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный результат.

text1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor\
 incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco\
  laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\
   cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia\
    deserunt mollit anim id est laborum.'
print('The number of suggestions in the text = ', text1.count('.' or '!' or '?'))

# Задание 6
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/

expression = input('Enter an arithmetic expression (eg, 23+12): ')
if expression.find('+') != -1:
    n = expression.find('+')
    num1 = int(expression[:n])
    num2 = int(expression[n+1:len(expression)])
    print(expression, '=', num1 + num2)
if expression.find('-') != -1:
    n = expression.find('-')
    num1 = int(expression[:n])
    num2 = int(expression[n+1:len(expression)])
    print(expression, '=', num1 - num2)
if expression.find('*') != -1:
    n = expression.find('*')
    num1 = int(expression[:n])
    num2 = int(expression[n+1:len(expression)])
    print(expression, '=', num1 * num2)
if expression.find('/') != -1:
    n = expression.find('/')
    num1 = float(expression[:n])
    num2 = float(expression[n+1:len(expression)])
    if num2 == 0:
        print("Error: division by zero.")
    else:
        print(expression, '=', num1 / num2)
