# def nameUpper(name):
#     return 'user' + name.upper()
#
#
# def nameLower(name):
#     return 'user' + name.lower()
#
#
# def makeLogin(userName, maker):
#     return maker(userName)
#
#
# name = "qwerty"
# print(makeLogin(name, nameLower))
# print(makeLogin(name, nameUpper))
#
# adminPass = 'admin'
#
#
# def userLogIn(userLog, userPass):
#     if (userLog.lower() == 'admin') and (userPass.lower() == adminPass):
#         print("Welcome!")
#     else:
#         print('Wrong data')
#
#
# def changePass(userLog, userPass):
#     global adminPass
#     if (userLog.lower() == 'admin') and (userPass.lower() == adminPass):
#         adminPass = input("Input new pass ")
#     else:
#         print('wrong data')
#
#
# def userAction(login, passw, action):
#     return action(login, passw)
#
#
# #
# # userAc = input('1- logIn  2- Change pass')
# # if userAc == '1':
# #     userAction('admin', 'admin', userLogIn)
# # elif userAc == '2':
# #     userAction('admin', 'admin', changePass)
# #
# # print(adminPass)
#
# prices = [100, 345, 66, 6, 4, 24, 655, 1]
# expensive = list(filter(lambda x: x > 100, prices))
# print(prices)
# print(expensive)
#
# userLogs = ['123user34', 'Userqwerty', '234dffdf', 'User-23', 'ADMIN']
#
#
# def checkLog(user):
#     if user.lower().find('user') != -1:
#         return True
#     else:
#         return False
#
#
# selectedUser = list(filter(checkLog, userLogs))
# print(selectedUser)
#
# userLogsLow = []
#
# print(userLogs)
#
# for log in userLogs:
#     userLogsLow.append(log.lower())
# print(userLogsLow)
#
# print(list(map(str.lower, userLogs)))
#
myValues = ['2.3', '12', '34', '345', '1']
print(myValues)

myNumbers = list(map(float, myValues))
print(myNumbers)

myDigits = list(map(lambda x: int(x[0]), myValues))
print(myDigits)
#
# pizzaTypes = ['4Cheese', "Meat", 'Sicilian']
# print(pizzaTypes)
#
#
# def modifyPizzaTypes(pizzaType):
#     return pizzaType + ' Pizza'
#
#
# pizzaNames = list(map(modifyPizzaTypes, pizzaTypes))
# print(pizzaNames)
#
numlist1 = [10, 20, 30]
numlist2 = [1, 2, 3]

result = map(lambda a, b: a ** b, numlist1, numlist2)
print(list(result))
#
# userLogs = ['123user34', 'Userqwerty', '234dffdf', 'User-23', 'ADMIN']
# userPass = ['123', '4234', '23423', '23454', 'asdfas']
#
# print(list(zip(userLogs, userPass)))
#
# for log, passw in zip(userLogs, userPass):
#     print(f"log: {log}, pass: {passw}")
#
# list1 = [1, 2, 3, 4, 5]
#
# print(list(zip(list1)))
#
# from functools import reduce
#
# nums = []
#
# result = reduce(lambda a, b: a + b, nums, 0)
# print(result)
#
# words = ['python', 'is', 'cool']
#
# sentence = reduce(lambda x, y: x + y if x == '' else x + ' ' + y, words, "")
# print(sentence)

# mylist = [1, 2, 3, 4, 5]
# result = map(lambda a: a ** 2, mylist)
# print(list(result))
#
# mylist2 = ["apple", "banana", "cherry"]
# result = map(lambda a: len(mylist2), mylist2)
# print(list(result))
#
# mylist3 = [1, 2, 3, 4, 5]
# newList = list(filter(lambda x: x % 2, mylist3))
# print(mylist3)
# print(newList)



