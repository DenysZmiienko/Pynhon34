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

import sys
class Contact:
    def __init__(self,first_name,last_name,email,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def showInfoContact(self):
        return (f"Contact: first_name: {self.first_name}, last_name {self.last_name}, email {self.email},"
                f" phone_number {self.phone_number}")

class OptimizedContact:
    __slots__ = ("first_name","last_name","email","phone_number")
    def __init__(self,first_name,last_name,email,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

contact1 = Contact("Alex", "Korobka", 'alex.korobka@ukr.net', "+38 099 111 11 11")
contact2 = Contact("Fil", "Pulaskis", 'f.pul@fin.net', "+51 033 222 22 22")
print("Without __slots__")
print(contact1.showInfoContact())
print(contact2.showInfoContact())
print("WITH __slots__")
print("Contact: ", contact1.__dict__)
print("Contact: ", contact2.__dict__)
print("Size of an object in bytes Without __slots__")
print(sys.getsizeof(contact1.showInfoContact()))
print(sys.getsizeof(contact2.showInfoContact()))
print("Size of an object in bytes WITH __slots__")
print(sys.getsizeof(contact1))
print(sys.getsizeof(contact2))

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

import random
from abc import ABC, abstractmethod

class ShipABC(ABC):
    def __init__(self, name,country):
        self.name = name
        self.country = country

    def showInfo(self):
        print(f"Name: {self.name}\nCountry:{self.country}")

    @abstractmethod
    def fire(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Battleship(ShipABC):
    def __init__(self,name,country):
        super().__init__(name,country)

    def fire(self):
        pass

    def move(self):
        print(f"The player has gone to sea and is ready to attack and repel the attack!")

    def showInfo(self):
        super().showInfo()

class Submarine(ShipABC):
    def __init__(self, name, country):
        super().__init__(name, country)

    def fire(self):
        pass

    def move(self):
        print(f"The player has gone to sea and is ready to attack and repel the attack!")

    def showInfo(self):
        super().showInfo()

class Player(Battleship, Submarine):
    def __init__(self, name_p, name, country, health, attack, defense, treasure, gold):
        super().__init__(name, country)
        self.name_p = name_p
        self.health = health
        self.attack = attack
        self.defense = defense
        self.treasure = treasure
        self.gold = gold

    def is_alive(self):
        return self.health > 0

    def print_status(self):
        print(f"{self.name}: Health = {self.health}, Attack = {self.attack}, Defense = {self.defense},"
              f" Treasure = {self.treasure}")

class Enemy(Battleship, Submarine):
    def __init__(self,name_e, name, country, health, attack, defense, gold_reward):
        super().__init__(name, country)
        self.name_e = name_e
        self.name = name
        self.health = health
        self.attacking = attack
        self.defense = defense
        self.gold_reward = gold_reward

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def print_status(self):
        print(f"{self.name}: Health = {self.health}, Attacking = {self.attacking},"
              f" Defense = {self.defense}")

class Game():

    def __init__(self):
        self.players = []

    def addPlayer(self, *args):
        for newPlayer in args:
            if isinstance(newPlayer, ShipABC):
                self.players.append(newPlayer)
            else:
                print("Error type of player!")

    def fire(self):
        print("Enemy", enemy.name, "attacks!")
        while player.is_alive() and enemy.is_alive():
            print("\n" + "-" * 100)
            player.print_status()
            enemy.print_status()
            print("-" * 100 + "\n")

            player_damage = max(0, player.attack - enemy.defense)
            enemy.take_damage(player_damage)
            print(f"You hit the {enemy.name} for {player_damage} damage.")

            if enemy.is_alive():
                enemy_damage = max(0, enemy.attack - player.defense)
                player.health -= enemy_damage
                print(f"The {enemy.name} strikes you for {enemy_damage} damage.")

            if player.is_alive():
                print("\nVictory! You have defeated the", enemy.name + "!")
                player.gold += enemy.gold_reward
                print(f"You loot {enemy.gold_reward} gold from the {enemy.name}.")
            else:
                print("\nYou have been slain by the", enemy.name + "!")
                print("Game Over")

    def move(self):
        if self.players:
            for players in self.players:
                players.move()
        else:
            print("Zero players")

player = Player("DENDY",'Submarine "Virginia"',"USA",50,50,30,30, 50)

enemy1 = Enemy("russian orc 1","Cruiser 'Moscow'", "russia", 2, 5, 10, 20)
enemy2 = Enemy("russian orc 2", "BDK 'Saratov'", "russia", 3, 5,10, 20)
enemy3 = Enemy("russian orc 3", "Submarine boat 'Rostov-on-Don'", "russia", 4, 5, 10, 20)

enemies = [enemy1, enemy2, enemy3]

print("\nWelcome to World of Warships!\n")

while player.is_alive():

    enemy = random.choice(enemies)
    newGame = Game()
    newGame.addPlayer(player)
    newGame.move()
    newGame.fire()
    if not input("Do you want to play another game? (yes/no): ").lower().startswith("y"):
        break