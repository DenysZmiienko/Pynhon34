# num = 1
# while num < 5:
#     print("num=", num)
#     num += 1
# else:
#     print("while ended")

# import time
# num = 1
# while True:
#     print(num)
#     num += 1
#     time.sleep(0.1)
#     if num == 20:
#         break
# else:
#     print("count end")

# import random
# floor = 1
# energy = random.randint(30,60)
# print(f"i am on the {floor} floor")
# while floor !=5:
#     step = 0
#     while step != 20:
#         step += 1
#         energy -= 1
#         if energy == 0:
#             print("i am tired")
#             energy +=30
#     floor +=1
#     print(f"now i am on {floor} floor")
# print("i am on the right flooor")

# i = 0
# start = 1
# end = 100
# while start < end:
#     start += 10
#     i += 1
# print("count iter", i)


# sum = 0
# i = 0
# while i < 20:
#     i += 1
#     sum += i
# print("sum=", sum)

# sum = 0
# i = 0
# count = 0
# while i < 20:
#     i += 1
#     sum += i
#     count += 1
# print("sum=", sum / count)
#
# while i < 30:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# import random
# rand_num = random.randint(1,10)
# user_num = 0
# tries = 5
# while rand_num != user_num:
#     user_num = int(input("enter num 1-10"))
#     tries -= 1
#     if tries == 0:
#         print("game over")
#         break
#     else:
#         if user_num < rand_num:
#             print("try bigger")
#         else:
#             print("try lover")
# else:
#     print("win")

# for i in range(10):
#     print(i)

# for i in range(10, 20):
#     print(i)

# for i in range(10, 20, 2):
#     print(i)

# for s in "hello":
#     print(s, end=" - ")

# for num in range(100):
#     print(num)
#     if num == 5:
#         break

# for num in range(100):
#     if num % 3 == 0:
#         continue
#     print(num)
#     if num == 20:
#         break

# num = int(input("Enter num"))
# for i in range(0, num):
#      print(i)

#2
# numStart = int(input("Enter numStart"))
# numEnd = int(input("Enter numEnd"))
# temp = 0
# if numStart > numEnd:
#     temp == numStart
#     numStart == numEnd
#     temp == numEnd
#
# for i in range(numStart, numEnd + 1):
#     print(i)
# for i in range(numStart, numEnd + 1):
#     if i % 2 == 0:
#         print(i)
# for i in range(numStart, numEnd + 1):
#     if i % 7 == 0:
#         print(i)

# numStart = int(input("Enter numStart"))
# numEnd = int(input("Enter numEnd"))
# sum = 0
# while numStart < numEnd:
#     numStart += 1
#     sum += numStart
# print("sum=", sum)

# num = int(input("Enter num"))
sum = 0
while num != 0:
    num = int(input("Enter num"))
    num += 1
    sum += num
    print(sum)