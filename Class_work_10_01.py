# myTuple = ('elem', 123, False, 2.4)
# print(myTuple)
# print(type(myTuple))
#
# myTuple2 = 'elem', 'elem2', 'elem3'
# print(myTuple2)
#
# myTuple3 = tuple(('Alex', 'Helen'))
# print(myTuple3)
#
# userTypes = ('admin', 'student', 'teacher', 'moderator')
# print(userTypes[0])
# print(userTypes[2])
# print(userTypes[-1])
# print(userTypes[1:3])
#
# # del userTypes
# type1, *type2 = userTypes
# print(type1, type2)
#
# for user in userTypes:
#     print(user)
#
# for i in range(len(userTypes)):
#     print((userTypes))
#
# allUser = userTypes + ('user1', 'user2')
# print(allUser)
#
# print('count', allUser.count('user1'))
#
# print(allUser.index('user1'))
#
# if 'user3' in allUser:
#     print(allUser.index('user3'))


# name_age = [("Анна", 22), ("Иван", 16), ("Мария", 20), ("Петр", 25)]
# sorted_name_age = list(filter(lambda x: x[1] > 18, name_age))
# print(sorted_name_age)

# mySet1 = {1, 2, 3}
# mySet2 = {'joy', 'boy', 'bill'}
# mySet3 = {23, 'god', False, 2.3, (5,6)}
# print(mySet1, mySet2, mySet3)
#
# mySet4 = set((10, 20, 30))
# print(mySet4)

# soldPhones = {'iphone11','iphone12','iphone13'}
# phones = {'iphone12','iphone13','iphone14'}
#
# print('soldPhones', soldPhones)
# print('phones', phones)
# print('intersection')
# print(soldPhones & phones)
# print(soldPhones.intersection((phones)))
#
# print('union')
# print(soldPhones | phones)
#
# print('diference')
# print(soldPhones - phones)
# print(phones - soldPhones)
# print(soldPhones.difference(phones))
#
# scores={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# print("Min score is", min(scores))
# print("Max score is", max(scores))
# print("Sum of scores:", sum(scores))
# print(sorted(scores))
#
# frozenA = frozenset(['Hanna','Joe','Kate'])
# frozenB = frozenset(['Bob', 'Joe', 'Jane', 'Kate', 'Jack'])
# print("frozenA:", frozenA)
# print("frozenB:", frozenB)
# print("Intersection of frozensets:")
# print(frozenA&frozenB)
# print(frozenA.intersection(frozenB))
# print("Union of frozensets:")
# print(frozenA|frozenB)
# print(frozenA.union(frozenB))
# print("Difference of two frozensets:")
# print(frozenB-frozenA)
# print(frozenB.difference(frozenA))
#
# allPizzaTypes=['Veggie', 'Pepperoni', 'Meat',
# 'Margherita', 'Meat', 'BBQ Chicken',
# 'Hawaiian', 'Veggie']
# uniquePizzaTypes = list(set(allPizzaTypes))
# print(uniquePizzaTypes)
# ['BBQ Chicken', 'Veggie','Meat', 'Margherita','Hawaiian', 'Pepperoni']

salers = [("Андрей", 5000), ("Марина", 3000), ("Иван", 8000), ("Елена", 6000)]
sorted_salers = sorted(salers, key=lambda x: x[1])
print(sorted_salers)

point1 = (3, 4)
point2 = (6, 8)
distans = ((point2[0] - point1[0]) , (point2[1] - point1[1]))
print('distans = ', distans)

produkt = [('Яблоки', 10), ('Молоко', 5), ('Хлеб', 3), ('Масло', 2)]
print('count', len(produkt))
total = sum(map(lambda x: int(x[1]), produkt))
print(total)

film = [('Интерстеллар', 2014, 'Кристофер Нолан'), ('Матрица', 1999, 'Лана Вачовски'),
    ('История игрушек', 1995, 'Джон Лассетер'), ('Гравитация', 2013, 'Альфонсо Куарон')]
sorted_film = list(filter(lambda x: x[1] > 2000, film))
print(sorted_film)
