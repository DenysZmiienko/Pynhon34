# Задание: Оптимизация хранения контактов в адресной книге
# 1. Создайте класс Contact, который будет представлять контакт в адресной книге.
# У этого класса должны быть следующие атрибуты:
# first_name: имя контакта.
# last_name: фамилия контакта.
# email: адрес электронной почты контакта.
# phone_number: номер телефона контакта.
# 2.Создайте несколько объектов класса Contact с разными контактами и заполните их данными.
# 3.Измерьте объем памяти, занимаемый каждым объектом класса Contact с использованием функции sys.getsizeof().
# Запишите результаты.
# 4.Создайте новый класс OptimizedContact, который также представляет контакт в адресной книге,
# но использует атрибут __slots__ для определения атрибутов. Атрибуты __slots__ должны содержать те же поля,
# что и в классе Contact.
# 5.Создайте несколько объектов класса OptimizedContact и заполните их данными.
# 6.Измерьте объем памяти, занимаемый каждым объектом класса OptimizedContact с использованием sys.getsizeof().
# Запишите результаты.
# 7.Сравните объемы памяти, используемые объектами класса Contact и OptimizedContact.
# Какие выводы можно сделать о разнице в потреблении памяти?

# import sys
# class Contact:
#     def __init__(self,first_name,last_name,email,phone_number):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone_number = phone_number
#
#     def showInfoContact(self):
#         return (f"Contact: first_name: {self.first_name}, last_name {self.last_name}, email {self.email},"
#                 f" phone_number {self.phone_number}")
#
# class OptimizedContact:
#     __slots__ = ("first_name","last_name","email","phone_number")
#     def __init__(self,first_name,last_name,email,phone_number):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone_number = phone_number
#
# contact1 = Contact("Alex", "Korobka", 'alex.korobka@ukr.net', "+38 099 111 11 11")
# contact2 = Contact("Fil", "Pulaskis", 'f.pul@fin.net', "+51 033 222 22 22")
# print("Without __slots__")
# print(contact1.showInfoContact())
# print(contact2.showInfoContact())
# print("WITH __slots__")
# print("Contact: ", contact1.__dict__)
# print("Contact: ", contact2.__dict__)
# print("Size of an object in bytes Without __slots__")
# print(sys.getsizeof(contact1.showInfoContact()))
# print(sys.getsizeof(contact2.showInfoContact()))
# print("Size of an object in bytes WITH __slots__")
# print(sys.getsizeof(contact1))
# print(sys.getsizeof(contact2))

# Задание: Разработка игры "Бои кораблей"
# 1. Создайте абстрактный базовый класс Ship с абстрактными методами:
# __init__(): инициализация корабля с его характеристиками.
# fire(): абстрактный метод для атаки других кораблей.
# move(): абстрактный метод для перемещения корабля.
# 2. Создайте два класса, Battleship и Submarine, которые наследуются от Ship.
# Реализуйте их конструкторы, а также методы fire() и move().
# 3. Создайте класс Player, который будет представлять игрока. Игрок должен иметь атрибуты, такие как имя и список кораблей,
# которыми он управляет.
# 4. Создайте класс Game, который будет управлять ходом игры.
# Этот класс должен иметь методы для регистрации игроков, управления ходом,
# проверки завершения игры и т. д.
# 5. Создайте несколько объектов классов Battleship и Submarine, и раздайте их игрокам.
# 6. Реализуйте игровую логику, включая ходы игроков, атаки, перемещение кораблей и т. д.
# 7. Завершите игру, когда один из игроков потеряет все корабли.
# 8. Подумайте о дополнительных функциях, которые могли бы сделать игру более интересной,
# таких как возможность улучшения кораблей,
# использование стратегии и так далее.
# Напишите краткое описание вашей игры и как абстрактные базовые классы помогли вам упростить разработку и обеспечить согласованный
# интерфейс для различных типов кораблей.

from abc import ABC, abstractmethod

class ShipABC(ABC):
    def __init__(self, name, appointment, speed, weapons):
        self.name = name
        self.appointment = appointment
        self.speed = speed
        self.weapons = weapons

    def showInfo(self):
        print(f"Name: {self.name}\nAppointment:{self.appointment}\nSpeed:{self.speed}\nWeapons:{self.weapons}")

    @abstractmethod
    def fire(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Battleship(ShipABC):
    def __init__(self, name, appointment, speed, weapons,size):
        super().__init__(name, appointment, speed, weapons)
        self.size = size

    def fire(self):
        print(f"I am a warship and attack with attrition, missiles and torpedoes!")

    def move(self):
        print(f"The ship moves only on the surface")

    def showInfo(self):
        super().showInfo()
        print(f"Size:{self.size}")

class Submarine(ShipABC):
    def __init__(self, name, appointment, speed, weapons, generation):
        super().__init__(name, appointment, speed, weapons)
        self.generation = generation

    def fire(self):
        print(f"I'm a submarine and I attack with missiles and torpedoes!")

    def move(self):
        print(f"The submarine moves both underwater and on the surface")

    def showInfo(self):
        super().showInfo()
        print(f"Size:{self.generation}")

class Game:
    def __init__(self):
        self.players = []

    def addPlayer(self, *args):
        for newPlayer in args:
            if isinstance(newPlayer, ShipABC):
                self.players.append(newPlayer)
            else:
                print("Error type of player!")

    def showPlayers(self):
        if self.players:
            for players in self.players:
                players.showInfo()
        else:
            print("Zero players")

    def fight(self):
        if self.players:
            for players in self.players:
                players.atack()
        else:
            print("Zero players")


battleship1 = Battleship("Getman Saghaydachny", "Fregat", 25, "Rockets, cannon artillery", 180)
battleship2 = Battleship("Smashing", "Destroyer", 30, "Torpedoes, cannon artillery", 67)
submarine1 = Submarine("Virginia", "Multipurpose nuclear submarine", 32, "Mine-torpedo and missile weapons", 4)
submarine2 = Submarine("Dolphin", "Diesel-electric submarine", 20, "Torpedoes, cannon artillery", 4)