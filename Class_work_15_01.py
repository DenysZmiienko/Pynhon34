# myDict1= {'key1': 1, 'key2': 2, 'key3': 3}
# myDict2= {1: 'student', 2: 'admin'}
# print(myDict1)
# print(myDict2)
#
bookDict = {
    'author':'Eric Matthes',
    'title':'Python Crash Course',
    'price':14.43,
    'reading age':'12 years and up',
    'language':'English'
}
print(bookDict)
#
# myDict3 = dict([("a", 111), ("b", 222)])
# print(myDict3)
#
# myDict4 = dict([["a", 111], ["b", 222]])
# print(myDict4)
#
# keyList = ['c','d']
# valueList = [111,222]
# myDict6 = dict(zip(keyList,valueList))
# print(myDict6)
#
# print('len ', len(bookDict))
#
# print(bookDict['author'])
#
key = 'author'
if key in bookDict:
    print(bookDict[key])
#
# bookDict['pages'] = 200
#
for key,val in bookDict.items():
    print("key: ", key)
    print("value: ", len(key))
#
# print(bookDict.get('author'))
# print(bookDict.get('page'))
# print(bookDict.get('page',0))
#
# bookDict.update([('pages', 600), ('discount', True)])
# print(bookDict)
# bookDict.update([['pages', 700], ('online', False)])
# print(bookDict)
#
# studGr1={'Joe':75,'Bob':92}
# studGr2={'Kate':62,'Joe':90, 'Jack':84}
# print(studGr1) #{'Joe': 75, 'Bob': 92}
# studGr1.update(studGr2)
# print(studGr1) #{'Joe': 90, 'Bob': 92, 'Kate': 62,'Jack': 84}
#
# studGr2={'Kate':62,'Joe':90, 'Jack':84}
# del studGr2['Jack']
# print(studGr2) #{'Kate': 62, 'Joe': 90}
#
# print(list(bookDict.keys()))
# print(list(bookDict.values()))
# print(list(bookDict.items()))
#
# delItem = bookDict.pop("price")
# print("item {} was deleted".format(delItem))
# print(bookDict)
#
# delItem = bookDict.pop("discount","None")
# print(delItem)
#
# bookDict2 = bookDict.copy()
# print(bookDict2)
#
# users = [
#     {'name': 'Hanna', 'age': 10, 'login':'user56'},
#     {'name': 'Mark', 'age': 15, 'login':'usER111'},
#     {'name': 'Jane', 'age': 17, 'login':'superGirl'},
#     {'name': 'Jack', 'age': 7, 'login':'userJack'}
# ]
#
# # keyName =input("Input info type:")
# # keyValue =input("Input info value:")
# keyName = 'name'
# keyValue = 'Hanna'
# isElementFound = False
# for user in users:
#     if user.get(keyName) == keyValue:
#         print("Element is found!")
#         # for key,val in user.items():
#         #     print("{}:{}".format(key,val))
#         isElementFound = True
#         break
# if isElementFound == False:
#     print("Element is not found!")
#
# users = [
#     {'name': 'Hanna', 'age': 10, 'login':'user56'},
#     {'name': 'Mark', 'age': 15, 'login':'usER111'},
#     {'name': 'Jane', 'age': 17, 'login':'superGirl'},
#     {'name': 'Jack', 'age': 7, 'login':'userJack'}
# ]
# sortedUsersbyName=sorted(users, key=lambda x: x['name'])
# print("Users list sorted by name:")
# for user in sortedUsersbyName:
#     for key,value in user.items():
#         print("{}:{}".format(key,value))
#
#
# users2 = [
#     {'name': 'Hanna', 'age': 10, 'login':'user56'},
#     {'name': 'Mark', 'age': 15, 'login':'usER111'},
#     {'name': 'Jane', 'age': 17, 'login':'superGirl'},
#     {'name': 'Jack', 'age': 7, 'login':'userJack'}
# ]
# users12=list(filter(lambda user: user['age'] >12, users2))
# # for user in users12:
# #     for key,val in user.items():
# #         print("{}:{}".format(key,val))
# print(users12)

# d1 = dict()
# d1 = [
#     {'name': 'Hanna', 'age': 10, 'login':'user56'},
#     {'name': 'Mark', 'age': 15, 'login':'usER111'},
#     {'name': 'Jane', 'age': 17, 'login':'superGirl'},
#     {'name': 'Jack', 'age': 7, 'login':'userJack'}
# ]
# print(d1)
# keyName = input("Input info type:")
# keyValue = input("Input info value:")
# isElementFound=False
# for user in d1:
#     if user.get(keyName)==keyValue:
#         print("Element is found!")
#         for key,val in user.items():
#             print((key,val))
#     isElementFound=True
#     break
#     if isElementFound==False:
#         print("Element is not found!")
#
bookDict = {
    'author':'Eric Matthes',
    'title':'Python Crash Course',
    'price':14.43,
    'reading age':'12 years and up',
    'language':'English'
}

key = 'author'
for key,val in bookDict.items():
    print("key: ", key)
    print("value: ", len(key))