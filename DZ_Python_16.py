# Задание 1
# К уже реализованному классу «Дробь» добавьте статический метод,
# который при вызове возвращает количество созданных объектов класса «Дробь».



# Задание 2
# Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и # для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температуры и # возвращать это значение с помощью статического метода.




# Задание 3
# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о кофемашине),
# класс Blender (содержит информацию о блендере), класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые  для работы методы.

class Device:
    def __init__(self, manufacturer, release_hour, power, color):
        self.manufacturer = manufacturer
        self.release_hour = release_hour
        self.power = power
        self.color = color

    def show_info(self):
        print(f'Manufacturer: {self.manufacturer}, Release hour: {self.release_hour},'
              f' Power: {self.power}, Color: {self.color}')

    def destination(self):
        pass

class Blender(Device):
    def __init__(self,manufacturer, release_hour, power, color, number_nozzles):
        super().__init__(manufacturer, release_hour, power, color)
        self.number_nozzles = number_nozzles

    def show_info(self):
        super().show_info()
        print("The blender has the appropriate number of nozzles:", self.number_nozzles)

    def destination(self):
        print("This electric appliance intended for grinding food, preparing emulsions, mashed potatoes,"
              " whipping drinks, mousses, etc., as well as crushing ice.")

class CoffeeMachine(Device):
    def __init__(self,manufacturer, release_hour, power, color, number_coffee_drinks):
        super().__init__(manufacturer, release_hour, power, color)
        self.number_coffee_drinks = number_coffee_drinks

    def show_info(self):
        super().show_info()
        print("The coffee machine can prepare the following number of coffee drinks:", self.number_coffee_drinks)

    def destination(self):
        print("This coffee machine will prepare the most exquisite coffee drinks for you")

class MeatGrinder(Device):
    def __init__(self,manufacturer, release_hour, power, color, number_nozzles_grinding_meat):
        super().__init__(manufacturer, release_hour, power, color)
        self.number_nozzles_grinding_meat = number_nozzles_grinding_meat

    def show_info(self):
        super().show_info()
        print("The meat grinder has the following number of nozzles for grinding meat:", self.number_nozzles_grinding_meat)

    def destination(self):
        print("The meat grinder is an electromechanical device for making minced meat and grinding other types of products.")

print("Blender: ")
myBlender = Blender("Bosch", 2022, 1800, "black", 4)
myBlender.show_info()
myBlender.destination()
print()
print("Coffee Machine: ")
myCoffeeMachine = CoffeeMachine("DeLonghi", 2023, 2000, "black", 15)
myCoffeeMachine.show_info()
myCoffeeMachine.destination()
print()
print("Meat Grinder: ")
myMeatGrinder = MeatGrinder("Tefal", 2021, 1500, "black", 3)
myMeatGrinder.show_info()
myMeatGrinder.destination()


# Задание 4
# Создайте класс Ship, который содержит информацию о корабле.
# С помощью механизма наследования, реализуйте класс Frigate (содержит информацию о фрегате),
# класс Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы.

class Ship:
    def __init__(self, manufacturer, name,  country, knot_speed, sediment):
        self.manufacturer = manufacturer
        self.name = name
        self.country = country
        self.knot_speed = knot_speed
        self.sediment = sediment


    def show_info(self):
        print(f'Manufacturer: {self.manufacturer}, Name: {self.name}, Сountry: {self.country},'
              f' Knot speed: {self.knot_speed}, Sediment: {self.sediment}')

    def destination(self):
        pass

class Frigate(Ship):
    def __init__(self, manufacturer, name,  country, knot_speed, sediment, number_depth_charge_devices):
        super().__init__(manufacturer, name,  country, knot_speed, sediment)
        self.number_depth_charge_devices = number_depth_charge_devices

    def show_info(self):
        super().show_info()
        print("Number of depth charge devices:", self.number_depth_charge_devices)

    def destination(self):
        print("A frigate is a large anti-submarine ship or sea vessel to perform patrol functions.")

class Destroyer(Ship):
    def __init__(self, manufacturer, name,  country, knot_speed, sediment, radius_action):
        super().__init__(manufacturer, name,  country, knot_speed, sediment)
        self.radius_action = radius_action

    def show_info(self):
        super().show_info()
        print("Radius action destroyer:", self.radius_action)

    def destination(self):
        print("A destroyer is a rugged, maneuverable, and fast warship.")

class Сruiser(Ship):
    def __init__(self,manufacturer, name,  country, knot_speed, sediment, rocket_launchers):
        super().__init__(manufacturer, name,  country, knot_speed, sediment)
        self.rocket_launchers = rocket_launchers

    def show_info(self):
        super().show_info()
        print("Number of rocket launchers:", self.rocket_launchers)

    def destination(self):
        print("A cruiser is the most versatile vessel.")

print("Frigate: ")
myFrigate = Frigate("Ukraine", ' Hetman Sahaidachny', 1992, "32", "4,7 m", 22)
myFrigate.show_info()
myFrigate.destination()
print()
print("Destroyer: ")
myDestroyer = Destroyer("Ingalls Shipbuilding","USS Gravely", "USA", 232, "9,4 m", "4980 mile", )
myDestroyer.show_info()
myDestroyer.destination()
print()
print("Сruiser: ")
myСruiser = Сruiser("Ukraine","Ukraine", "Ukraine", "8,4 m", "32", 16)
myСruiser.show_info()
myСruiser.destination()