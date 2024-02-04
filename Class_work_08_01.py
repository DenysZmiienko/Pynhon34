#
#
# def simplDecorstor(myfunc):
#     print("Hello! i am decorator")
#     def simpleWrapper():
#         print("Function start")
#         myfunc()
#         print("decorator ended")
#
#     return simpleWrapper
#
# def simplDecorstor_v2(myfunc):
#     print("Hello! i am decorator 2")
#     def simpleWrapper():
#         print("Function 2 start")
#         myfunc()
#         print("decorator 2 ended")
#
#     return simpleWrapper
# @simplDecorstor
# @simplDecorstor_v2
# def sayhello():
#     print("Hello")
import random
# newFunc = simplDecorstor(simplDecorstor_v2(sayhello))
# 1
# sayHelloAdvenst = simplDecorstor(sayhello)
# sayHelloAdvenst()

# sayhello()

# def simpleDecorator_v3(myFunction):
#     print("Hello! I'm 3 Decorator!")
#     def simpleWrapper():
#         print("Function 3 starts working...")
#         resutl=myFunction()
#         print("See you!")
#         return resutl
#     return simpleWrapper
# def calculateSum():
#     print("Welcome! Let's calculate...")
#     x=1
#     y=1
#     return x+y
# print(calculateSum())

# def simpleDecorator_v4(myFunction):
#     print("Hello! I'm Fourth Decorator!")
#     def simpleWrapper(argX, argY):
#         print("I've got {},{}. Function starts working...".
#         format(argX, argY))
#         resutl=myFunction(argX, argY)
#         print("See you!")
#         return resutl
#     return simpleWrapper
# def calculateSum_v1(a,b):
#     print("Welcome! Let's calculate...")
#     x=int(input("x: "))
#     y=int(input("y: "))
#     return x+y+a+b
#
# calculateSum_v1 = simpleDecorator_v4(calculateSum_v1)
# print(calculateSum_v1(3,4))


# pricesUSD=[100.34,35,67.99,25.5]
# print(pricesUSD)
#
# def toPriceNew(priceList):
#     return list(map(lambda x: x*39, priceList))
#
# def changePriceDecorator_v1(myFunction):
#     print("Hello! Let's change your prices...")
#     def simpleWrapper(argList):
#         print("I've got list of prices with {} elements.Function starts working...".
#         format(len(argList)))
#         resutl = myFunction(argList)
#         resutlwithDisc = list(map(lambda x: x*(1-0.15),resutl))
#         print("Let's set a discount..")
#         return resutlwithDisc
#     return simpleWrapper
# pricesToGRN = changePriceDecorator_v1(toPriceNew)
# print(pricesToGRN(pricesUSD))

# import time
#
# def checkTime(func):
#     def wrapper(*args):
#         srartTime = time.time()
#         result = func(*args)
#         print(f"forkinc time {time.time()} - {srartTime}")
#         return result
#     return wrapper
#
# @checkTime
# def testFunc():
#     print("func working")
#     time.sleep(1)
#
# testFunc()
#
# def avdTimeWorking(count):
#     def checkTime(func):
#         def wrapper(*args):
#             totalTime = 0
#             result = 0
#             for i in range(count):
#                 srartTime = time.time()
#                 result = func(*args)
#                 endTime = time.time()
#                 totalTime = totalTime + (endTime - srartTime)
#             print(f"avg time working - {totalTime / count}")
#             return result
#
#         return wrapper
#
#     return checkTime
#
# import random
# @avdTimeWorking(2)
# def func2():
#
#     time.sleep(random.randint(1, 3))
#
# func2()

# def simpleDecorator(myFunc):
#     print("Hello ! i am decorator !")
#
#     def simpleWrapper(args):
#         print("Function starts working with params:", args)
#         if type(args) == int:
#             return True
#         else:
#             return False
#         print("decorator ended")
#         return result
#
#     return simpleWrapper
#
# @simpleDecorator
# def num(x):
#     return x
# print(num(2.0))

# def simpleDecorator1(myFunc):
#     print("Hello ! i am  decorator !")
#
#     def simpleWrapper(*args, **kwargs):
#         print("Function  starts working with params:", args)
#         result = ':)'+ myFunc(*args, **kwargs)
#         print("decorator  ended")
#         return result
#
#     return simpleWrapper
#
# @simpleDecorator1
# def pref(a):
#     return a
# print(pref('Hello'))

ADMIN_TOKEN = 'fheje3$93m*fe!'

from functools import wraps
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated
