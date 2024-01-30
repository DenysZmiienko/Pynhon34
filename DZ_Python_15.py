# Задание 1
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных (сеттеры), вывода данных (геттеры), создайте конструктор с параметрами.

class Book:
    def __init__(self, title_book,year_publication,publisher,genre,author,price):

        self.__title_book = title_book
        self.__year_publication = year_publication
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def __del__(self):
        print("del book")

    def showInfoBook(self):
        return (f"Book: {self.__title_book} , {self.__year_publication} , {self.__publisher} ,"
                f" {self.__genre} , {self.__author} , {self.__price} ")

    def get_title_book(self):
        return self.__title_book

    def get_year_publication(self):
        return self.__year_publication

    def get_publisher(self):
        return self.__publisher

    def get_genre(self):
        return self.__genre

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def set_title_book(self, new_title_book):
        self.__title_book = new_title_book

    def set_year_publication(self, new_year_publication):
        self.__year_publication = new_year_publication

    def set_year_publisher(self, new_publisher):
        self.__publisher = new_publisher

    def set_genre(self, new_genre):
        self.__genre = new_genre

    def set_author(self, new_author):
        self.__author = new_author

    def set_price(self, new_price):
        self.__price = new_price

book1 = Book("Harry Potter and the Philosopher's Stone", 2021,
             "Bloomsbury", "Fantacy", "Rowling Joanne", "276 ₴")
book2 = Book('The Corrections', 2022, "4th Estate", "Action",
             "Franzen Jonathan", "280 ₴")

print(book1.showInfoBook())
print(book2.showInfoBook())

# Задание 2
# Создайте класс «Дробь». Необходимо хранить в закрытых полях класса: числитель и знаменатель.
# Реализуйте методы класса для ввода данных(сеттеры), вывода данных (геттеры), создайте конструктор с параметрами.
# Также создайте методы класса для выполнения арифметических операций (сложение, вычитание, умножение, деление, и т.д.).
# Протестируйте работу класса.

class Fraction:
    def __init__(self, numerator, denomerator):
        self.numerator = numerator
        self.denomerator = denomerator
        if self.denomerator == 0:
            return ("You can't divide by zero")

    def show(self):
        print(self.numerator, "/", self.denomerator)

    def Add(self, other):
        return (self.numerator*other.denomerator + self.denomerator*other.numerator) / (self.denomerator*other.denomerator)
    def Sub(self, other):
        return (self.numerator*other.denomerator - self.denomerator*other.numerator) / (self.denomerator*other.denomerator)
    def Mul(self, other):
        return (self.numerator*other.numerator / self.denomerator*other.denomerator)
    def Div(self, other):
        return (self.numerator*other.denomerator /  self.denomerator*other.numerator)

f1 = Fraction(2,4)
f2 = Fraction(3,2)
f3 = Fraction.Add(f1,f2)
f4 = Fraction.Sub(f1,f2)
f5 = Fraction.Mul(f1,f2)
f6 = Fraction.Div(f1,f2)

print((f1.show()), f2.show())
print(f"Addition =  {f3}")
print(f"Subtraction = {f4}")
print(f"Multiplication = {f5}")
print(f"Division = {f6}")

# Задание 3
# Цель задания: Разработать класс в Python, представляющий игрового персонажа, с уникальными особенностями и возможностями.
#
# Инструкции:
#
# Создайте класс с именем "GameCharacter".
# Определите атрибуты класса, которые отражают основные характеристики персонажа:
# Имя (name)
# Уровень (level)
# Здоровье (health)
# Сила атаки (attack_power)
# Защита (defense)
# Опыт (experience)
# Реализуйте конструктор класса, который инициализирует атрибуты персонажа с некоторыми начальными значениями.
# Добавьте метод для атаки, который будет учитывать силу атаки и защиту персонажа.
# Реализуйте метод для получения опыта. При достижении определенного количества опыта персонаж должен поднимать уровень, сопровождаемый увеличением характеристик.
# Создайте несколько экземпляров класса "GameCharacter" с разными характеристиками и протестируйте их, проводя атаки и получая опыт.

# class Unit:
#     def __init__(self, name, clan):
#         self.name = name
#         self.clan = clan
#         self.max_health = 100
#         self.min_health = 0
#         self.max_strength = 10
#         self.min_strength = 0
#         self.max_agility = 10
#         self.min_agility = 0
#         self.max_intelligence = 10
#         self.min_intelligence = 0
#
#     def read_unit(self):
#         read = self.name + " " + self.clan
#         return read.title()
#
#     def read_health(self):
#         if self.min_health + 10 > self.max_health:
#             self.max_health = 100
#         else:
#             self.min_intelligence += 10
#
#     def health_read(self):
#         print("У персонажа: " + str.read_health + " hp")
#
#
# class Mage(Unit):
#     def __init__(self, name, clan, air, fire, water):
#         super().__init__(name, clan, air, fire, water)
#
#     def intelligence_mage(self):
#         if self.min_intelligence + 1 < self.max_intelligence:
#             self.max_intelligence = 10
#         else:
#             self.min_intelligence += 10
#
#
# class Archer(Unit):
#     def __init__(self, name, clan, bow, crossbow):
#         super().__init__(name, clan, bow, crossbow)
#
#     def agility_archer(self):
#         if self.min_agility + 1 < self.max_agility:
#             self.max_agility = 10
#         else:
#             self.min_agility += 10
#
#
# class Knight(Unit):
#     def __init__(self, name, clan, sword, axe, pike):
#         super().__init__(self, name, clan, sword, axe, pike)
#
#     def agility_knight(self):
#         if self.min_strengthx + 1 < self.max_strength:
#             self.max_strength = 10
#         else:
#             self.min_strength += 10
#
#
# Eridan = Mage("Eridan", "Fresh", "fire")
# print(Eridan.read_unit())
# print(Eridan.intelligence_mage)
# Eridan.health_read()
#
# Erifan = Mage("Erifan", "Dradon", "water")
# print(Erifan.read_unit())
# print(Erifan.intelligence_mage)
# Erifan.health_read()
#
# Eren = Knight("Eren", "Fresh", "pike")
# print(Eren.read_unit())
# print(Eren.agility_knight)
# Eren.health_read()
#
# Selfi = Archer("Selfi", "Archer_best", "crossbow")
# print(Selfi.read_unit())
# print(Selfi.agility_archer)
# Selfi.health_read()
#
# Antalia = Mage("Antalia", "Fresh", "air")
# print(Antalia.read_unit())
# print(Antalia.intelligence_mage)
# Antalia.health_read()
#
# Enifar = Archer("Enifar", "Archer_best", "bow")
# print(Enifar.read_unit())
# print(Enifar.agility_archer)
# Enifar.health_read()
#
#
# class Unit:
#     def __init__(self, name, clan):
#         self.name = name
#         self.clan = clan
#         self.health = 100
#         self.power = 10
#         self.agility = 10
#         self.intellect = 10
#
#     def therapy(self):
#         if self.health < 100:
#             self.health += 10
#
#
# class Mage(Unit):
#     def __init__(self, name, clan, air, fire, water):
#         super().__init__(name, clan)
#         self.air = air
#         water
#         self.fire = fire
#         self.water = water
#
#     def augment(self):
#         if self.intellect < 10:
#             self.intellect += 1
#
#
# class Archer(Unit):
#     def __init__(self, name, clan, bow, crossbow):
#         super().__init__(name, clan)
#         self.bow = bow
#         self.crossbow = crossbow
#
#     def augment(self):
#         if self.agility < 10:
#             self.agility += 1
#
#
# class Knight(Unit):
#     def __init__(self, name, clan, sword, axe, pike):
#         super().__init__(self, name)
#         self.sword = sword
#         self.axe = axe
#         self.pike = pike
#
#     def augment(self):
#         if self.power < 10:
#             self.power += 1
#
#
# 0