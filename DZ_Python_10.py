# 1. Напишите декоратор, который ограничивает частоту вызова функции.
def function_call(frequency):
    def decorate(func):
        def wrapper(*args, **kwargs):
            for i in range(frequency):
                func(*args, **kwargs)
        return wrapper
    return decorate

@function_call(5)
def greetings():
    print("Нello world")

greetings()

# 2. Декоратор для логирования:
# Напишите декоратор, который записывает в лог информацию о вызове функции: её имя, переданные аргументы и результат выполнения.
#
def log_args(func):
    log = {}
    def wrapper(*args, **kwargs):
        if args not in log:
            log[args] = func(*args, **kwargs)
        return log[args]
    return wrapper

@log_args
def print_full_name(first_name, last_name):
    print("log_args;", first_name + '; ' + last_name)

print_full_name("Denys", "Zmiienko")

# 3.Декоратор для аутентификации:
# Создайте декоратор, который проверяет, авторизован ли пользователь, вызывающий функцию.
# Если пользователь не авторизован, декоратор должен выводить сообщение об ошибке.
def login_required(func):
    def wrapper_login_required(*args, **kwargs):
        if args is None:
            return "Error"
        return func(*args, **kwargs)
    return wrapper_login_required

@login_required
def log():
    return ("Only authorized users can call the function")

log()

# 4.Декоратор для определения типов аргументов и возвращаемого значения:
# Создайте декоратор, который проверяет,соответствуют ли аргументы и возвращаемое значение функции
# заданным типам данных, и выводит ошибку, если типы не совпадают.
def validate_input(*validations):
    def decorator(func):
        def wrapper_type_checking(*args, **kwargs):
            for i, val in enumerate(args):
                if i < len(validations):
                    if not validations[i](val):
                        raise ValueError(f"Invalid argument: {val}")
            for key, val in kwargs.items():
                if key in validations[len(args):]:
                    if not validations[len(args):][key](val):
                        raise ValueError(f"Invalid argument: {key}={val}")
            return func(*args, **kwargs)
        return wrapper_type_checking
    return decorator

@validate_input(lambda x: x > 0, lambda y: isinstance(y, str))
def divide_and_print(x, message):
    print(message)
    return x

divide_and_print(5, "Hello!")

# Дополнительно *
# Напишите декоратор, оптимизирующий работу декорируемой функции.
# Декоратор должен сохранять результат работы функции на ближайшие три запуска и
# вместо выполнения функции возвращать сохранённый результат. После трёх запусков
# функция должна вызываться вновь, а результат работы функции — вновь кешироваться.

# Подсказка:
# Создайте в декораторе переменную-кеш, сохраните в ней результат выполнения декорируемой функции.
#  Создайте в декораторе переменную, хранящую счётчик запросов. Пока значение счётчика ниже предельного —
# отдавайте результат, сохранённый в кеше. Когда число запросов к функции превысит предел и
# пора будет снова высчитывать результат выполнения функции — сбросьте счётчик,
# выполните декорируемую функцию и заново сохраните результат её выполнения в переменную-кеш.