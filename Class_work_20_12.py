# def sayHello():
#     print("Hello")
#
# sayHello()
# sayHello()
# sayHello()
#
# def helloUser(userName):
#     print("Hello ", userName)
#
# helloUser('Denis')
# name = 'qwerty'
# helloUser(name)
#
# def calculate(a,b,c):
#     print("Lets calculete ")
#     print(a + b * c)
#
# calculate(2,3,4)
#
# def calculate(a,b,c=1):
#     print("Lets calculete ")
#     print(a + b * c)
#
# calculate(2,3)
#
# def many(*args):
#     print(args)
#
# many(1,2,3,)
#
# def many(*args, **kwargs):
#     print(list(args))
#     for elem in args:
#         print(elem)
#
#     print(kwargs)
#
# many(1,2,3, x=1, y=3)
#
# def checkCustomer(customer, customers):
#     result = 0
#     print("Clients position on the list: ")
#     for i in range(len(customers)):
#         if customer == customers[i]:
#             print(i)
#             result +=1
#     return result
# customerList = ['dod', 'bob', 'ann']
#
# if checkCustomer('dod', customerList):
#     print('Cuctomer dod is', checkCustomer('bob', customerList))
#
# def checkLog(userLogin):
#     if userLogin == 'admin':
#         return userLogin.upper()
#     elif userLogin == 'user':
#         return userLogin.lower()
#     else:
#         return 'wrong login'
#
# login = checkLog(input("enter login")) + "*"
# print(login)
# print(checkLog("qwerty"))

# global_str = "qwerty"
# def testNamespace():
#     global global_str
#     global_str = "new data"
#     print(global_str)
#
# testNamespace()
# print(global_str)

import random

def outer():
    local_srt = "outer srt"
    def inner():
        nonlocal local_srt
        local_srt = "inner str"
        print(local_srt)
    inner()
    print(local_srt)

outer()

# def time(s,v):
#     print(s / v)
#
# time(22,3)
#
# def distance(v,t):
#     print(v * t)
#
# distance(5,5)


# def ret(num):
#     if num > 0:
#         return 'True'
#     else:
#         return 'False'
#
#
# ret()


# def print_numbers(n):
#     for i in range(1, n + 1):
#          print(i)
#
# print_numbers(6)
