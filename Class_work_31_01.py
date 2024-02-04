class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def show_info(self):
        print(f'{self.color} {self.name} стар на {self.age} лет')


class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def show_info(self):
        print(f'{self.color} {self.name} стар на {self.age} лет')


class Cow:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def show_info(self):
        print(f'{self.color} {self.name} стар на {self.age} лет')


class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def show_info(self):
        print(f'{self.color} {self.name} стар на {self.age} лет')

    def golos(self):
        pass


class Cat(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

    def show_info(self):
        super().show_info()
        print("breed:", self.breed)

    def golos(self):
        print("may may")


class Dog(Animal):
    pass


myCat = Cat("Barsik", 2, "red", "cat")
myCat.show_info()
myCat.golos()

import random


class Person:
    def __init__(self, firstname, lastname, age):
        # public prop
        self.firstname = firstname
        self.lastname = lastname
        # protected prop
        self._age = age
        # private prop
        self.__personId = random.randint(1, 100)

    # private  method
    def __showId(self):
        print(self.__personId)

    # public method
    def showInfo(self):
        self.__showId()
        return f"Person first name: {self.firstname}\nlastname: {self.lastname}\nage:{self._age}"

    #static method
    @staticmethod
    def sayHello():
        print("Hello !")

class Employee(Person):
    def __init__(self, firstname, lastname, age, salary):
        super().__init__(firstname, lastname, age)
        self.salary = salary

    def showInfo(self):
        return super().showInfo() + f"\nsalary:{self.salary}"

    def isRetiree(self):
        Person.sayHello()
        print(self.showInfo())
        if self._age > 60:
            print(f"{self.firstname} is retiree")
        else:
            print(f"{self.firstname} is not retiree")

    def changeAge(self, newAge):
        self._age = newAge


worker = Employee("Ilon", "Mask", 61, 1000)
# print(worker.showInfo())
worker.changeAge(35)
worker._age = 20
worker.isRetiree()
worker.sayHello()

Person.sayHello()
