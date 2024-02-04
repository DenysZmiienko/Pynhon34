# def factorialCalculation(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorialCalculation(n-1)
#
# print(factorialCalculation(5))
#
#
# def isStrPalindrom(myStr):
#     if len(myStr) == 0:
#         return True
#     else:
#         if myStr[0] == myStr[-1]:
#             return isStrPalindrom(myStr[1:-1])
#         else:
#             return False
#
# print(isStrPalindrom('madam'))
# print(isStrPalindrom('kaban'))
#
# def findMin(numberList):
#     if len(numberList) > 1:
#         return min(findMin(numberList[:-1]), numberList[-1])
#     else:
#         return numberList[0]
#
# print(findMin([4, 1, 0, -1]))
#
# def sum(n):
#     if n == 0:
#         return 1
#     else:
#         return n + sum(n-1)
#
# print(sum(5))
#
#
# def sumNumber(num):
#     if abs(num) < 10:
#         return abs(num)
#     else:
#         return abs(num) % 10 + sumNumber(num // 10)
#
# print(sumNumber(12345))
#
#
# myNumbers = [2, 2.5, 4.56, 23]
#
# def add10(x):
#     return x + 10
# for num in myNumbers:
#     print(add10(num))
#
#
# for num in myNumbers:
#     print((lambda x: x + 10)(num))
#
#
# students = [['Bob', 70],
#             ['Jane', 80],
#             ['Andy', 50]
# ]
# print(students)
# sortedSts = sorted(students, key=lambda x: x[1])
# print(sortedSts)
#
# grnToDollar = 38
# discount = 0.15
#
# priceDol = lambda x: x/grnToDollar * (1-discount)
# priceGrn1 = float(input("Input price1 in grn:"))
# print("price: {:.2f}$".format(priceDol(priceGrn1)))
# priceGrn2=float(input("Input price2 in grn:"))
# print("price: {:.2f}$".format(priceDol(priceGrn2)))
#
# userName = lambda firstName,lastName: f"Full user's name: {firstName.title()} {lastName.title()}"
# firstUserName=input("Input your first name:")
# lastUserName=input("Input your last name:")
# print(userName(firstUserName, lastUserName))

# myNumbers = [2, 3, 4, 5]
# for num in myNumbers:
#     print((lambda x: x * 2)(num))
#     print((lambda x: x ** 2)(num))
#
#
# myNumbers1 = [2, 3, 4, 5]
# for num in myNumbers1:
#     print(max(myNumbers1,key=lambda x: x))
#     print(min(myNumbers1,key=lambda x: x))


# myNumbers2 = [2, 3, 4, 5]
# for num in myNumbers2:
#     print(lambda x: sum(myNumbers2), myNumbers2)
# print(lambda x, y: x + y, [1, 2, 3, 4, 5])

myNumbers2 = [2, 3, 4, 5]
sum = (lambda x: sum(x))(myNumbers2)
print(sum)