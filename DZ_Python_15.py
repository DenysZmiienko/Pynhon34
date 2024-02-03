# Задание 1
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных (сеттеры), вывода данных (геттеры), создайте конструктор с параметрами.
#
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
# Реализуйте метод для получения опыта. При достижении определенного количества опыта персонаж должен поднимать уровень,
# сопровождаемый увеличением характеристик. Создайте несколько экземпляров класса "GameCharacter" с разными
# характеристиками и протестируйте их, проводя атаки и получая опыт.

class GameCharacter:
    def __init__(self, name, level, health, attack_power, defense, experience):
        self.name = name
        self.level = level
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.experience = experience

    def __del__(self):
        print()

    def showGameCharacter(self):
        return (f"Unit name: {self.name} , Unit level: {self.level} , Unit health: {self.health} ,"
                f"Unit attack power: {self.attack_power} , Unit defense: {self.defense} , Unit experience: {self.experience}")

    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    def get_level(self):
        return self.level
    def set_level(self, new_level):
        self.level = new_level

    def get_health(self):
        return self.health
    def set_health(self, new_health):
        self.health = new_health

    def get_attack_power(self):
        return self.attack_power
    def set_attack_power(self, new_attack_power):
        self.attack_power = new_attack_power

    def get_defense(self):
        return self.defense
    def set_defense(self, new_defense):
        self.defense = new_defense

    def get_experience(self):
        return self.experience
    def set_experience(self, new_experience):
        self.experience = new_experience

    def augment_attack_power(self):
        if self.attack_power < 100:
            self.attack_power += 1

    def augment_defense(self):
        if self.defense < 100:
            self.defense += 1

    def augment_level(self):
        if self.experience > 20:
            self.level += 1

    def therapy(self):
        if self.health < 100:
            self.health += 10

Unit1 = GameCharacter("Captain America", 5, 57, 80, 60, 67 )
Unit2 = GameCharacter("Iron Man", 6, 60, 76, 65, 66)
Unit3 = GameCharacter("Spider man", 4, 70, 55, 45, 41)

print(Unit1.showGameCharacter())
print(Unit2.showGameCharacter())
print(Unit3.showGameCharacter())

