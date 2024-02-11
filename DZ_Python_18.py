# 1. Задача: Создать класс, который использует метод класса для генерации уникальных идентификаторов для экземпляров.
# Инструкции:
# Создайте класс UniqueID.
# Добавьте атрибут класса next_id, который будет служить счетчиком для генерации уникальных идентификаторов.
# Создайте метод класса generate_id, который будет генерировать и возвращать уникальный идентификатор,
# инкрементируя счетчик next_id. Создайте несколько экземпляров класса UniqueID и вызовите метод generate_id
# для каждого из них, чтобы получить уникальные идентификаторы.

class UniqueID():
    next_id = 0
    unique_id = 0
    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        UniqueID.next_id += 1

    @classmethod
    def generate_id(cls):
        cls.unique_id += 1
        return cls.unique_id
    @classmethod
    def count(cls):
        print("Number of unique objects: ", cls.next_id)

obj1 = UniqueID()
obj2 = UniqueID()
obj3 = UniqueID()
print("Unique identifier of 1 object:", obj1.id)
print("Unique identifier of 2 object:", obj2.id)
print("Unique identifier of 2 object:", obj3.id)
UniqueID.count()

# 2.Требуется создать класс "Фильм", в котором будет использоваться класс-метод с именем "средний_рейтинг",
# который будет вычислять средний рейтинг всех фильмов, созданных с использованием этого класса.Так же
# реализуйте функцию для вывода рейтинга всех фильмов и функцию для вывода имен.

class Movie:
    movies = []

    def __init__(self, name, age, rating):
        self.name = name
        self.age = age
        self.rating = rating

    def print_data(self):
        return "Movie: " + self.name + " " + str(self.age) + " " + str(self.rating)

    @classmethod
    def all_data(cls):
        return '\n'.join(e.print_data() for e in cls.movies)

    @classmethod
    def avr_rating(cls):
        return sum(e.rating for e in cls.movies) / len(cls.movies)

class Action(Movie):

    def __init__(self, name, age, rating, main_actor):
        super().__init__(name, age, rating)
        self.main_actor = main_actor
        super().movies.append(self)

    def print_data(self):
        return "Action: " + self.name + " " + str(self.age) + " " + str(
            self.rating) + " " + self.main_actor

class Comedy(Movie):

    def __init__(self, name, age, rating, director):
        super().__init__(name, age, rating)
        self.director = director
        super().movies.append(self)

    def print_data(self):
        return "Comedy: " + self.name + " " + str(self.age) + " " + str(self.rating) + " " + self.director

move1 = Action('The Green Mile', 1999, 9.1, 'Tom Hanks')
move2 = Comedy('The Shawshank Redemption', 1994, 9.0, 'Frank Darabont')

print("Film catalog:")
print(Movie.all_data())
print("Average rating: ",Movie.avr_rating())

# 3.Используя механизм множественного наследования разработайте класс “Человек”.
# Должны быть классы “Мозг», «Сердце»,«Ноги» и т.д.

class Brain:
    def __init__(self, brain):
        self.brain = brain
    def showInfo(self):
        print("Brain: {}".format(self.brain))

class Heart:
    def __init__(self, heart):
        self.heart = heart

    def showInfo(self):
        print("Heart: {}".format(self.heart))

class Hands:
    def __init__(self, hands):
        self.hands = hands

    def showInfo(self):
        print("Hands: {}".format(self.hands))
class Legs:
    def __init__(self, legs):
        self.legs = legs

    def showInfo(self):
        print("Legs: {}".format(self.legs))
class Human(Brain,Heart,Hands,Legs):
    def __init__(self, brain, heart, hands, legs):
        Brain.__init__(self, brain)
        Heart.__init__(self, heart)
        Hands.__init__(self, hands)
        Legs.__init__(self, legs)

human = Human("Brain", "Heart", "Hands", "Legs")
human.showInfo()
print(Human.mro())
