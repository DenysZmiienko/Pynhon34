#------------- 1
# try:
#     amount = int(input("Enter the amoumt of recived items - "))
#     item_type = input("Enter type of item - ")
#     parts_number = int(input("Enter the numner of parts - "))
#     parts = amount / parts_number
# except:
#     print("Amount should de an integer!")

#-------------- 2
# try:
#     amount = int(input("Enter the amoumt of recived items - "))
#     item_type = input("Enter type of item - ")
#     parts_number = int(input("Enter the numner of parts - "))
#     parts = amount / parts_number
# except ValueError:
#     print("Amount should de an integer!")
# except ZeroDivisionError:
#     print("we cannot by zero")
# except Exception:
#     print("we have some error")
# else:
#     print("Your data is complete")
# finally:
#     print("program is finished")

#----------------- 3
# try:
#     amount = int(input("Enter the amoumt of recived items - "))
#     item_type = input("Enter type of item - ")
#     parts_number = int(input("Enter the numner of parts - "))
#     parts = amount / parts_number
# except (ValueError, ZeroDivisionError, TypeError):
#     print("we have some error enter value!")
# except Exception:
#     print("we have some error")

#-------------------- 4

# try:
#     x = 1/0
# except Exception as ex:
#     print("we have some error - ", ex.args)
#     print(type(ex).__name__)

# try:
#     raise ValueError("you make some mistake")
# except BaseException as ex:
#     print(ex)
#     print(type(ex).__name__)

# Напишите программу, которая запрашивает двацелых числа x и y,
# после чего вычисляет и выводитзначение x в степени y.

# try:
#     num1 = int(input("Enter num 1 - "))
#     num2 = int(input("Enter num 2 - "))
#     rez = num1 ** num2
#     print(rez)
# except ValueError:
#     print("Amount should de an integer!")

# try:
#     month = int(input("Enter month 1-12"))
#     if month > 0 and month < 13:
#         if month == 1:
#             print("January")
#         elif month == 2:
#             print("February")
#         elif month == 3:
#             print("March")
#         elif month == 4:
#             print("April")
#         elif month == 5:
#             print("May")
#         elif month == 6:
#             print("June")
#         elif month == 7:
#             print("July")
#         elif month == 8:
#             print("August")
#         elif month == 9:
#             print("September")
#         elif month == 10:
#             print("October")
#         elif month == 11:
#             print("November")
#         elif month == 12:
#             print("December")
# except ValueError:
#     print("Enter month 1-12")



num = input("Enter number: ")
try:
    while type(num) != int:
        num = int(num)
except ValueError:
    print("Enter correct number")
    num = input("Enter number: ")
else:
    print("OK")