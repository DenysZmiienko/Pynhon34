# myStr = "Python the best language in the world!"
# str2 = 'Javascript also cool'
# print(id(str2))
# str2 = "new str"
# print(f"str1 - {myStr}")
# print(f"str2 - {str2}")
#
# print(id(str2))
#
# str = 'hello'
#
# print(str + " " + str2)
# print('1' * 3)
#
# if 'h' in str:
#     print('yes')
#
# print(myStr[0])
# print(myStr[5])
# print(myStr[len(myStr)-1])
# print(len(myStr))
# print(myStr[-1])
#
# print(myStr[0:6])
#
# myStr="python was created in the late 1980's python by Guido van Rossum."
# print(myStr)
# print(myStr.capitalize())
# print(myStr.title())
# print(myStr.swapcase())
# print(myStr.lower())
# print(myStr.upper())
#
# print(myStr.find('python', 20, 25))
# print(myStr.rfind('python'))
#
# print(myStr.startswith('python'))
#
# num1 = '123'
# num = '123'
# print(num.isdigit())
# print(int(num1))
#
# str = 'qwerty'
# print(str2.islower())
# print(' g'.isspace())
#
# print('   str   '.strip())
#
# print(myStr.split())
#
# print(''.join('1','2','3'))
#
# print('123'.center(11,'-'))

import string
import random

userLogin = ''.join(random.sample(string.ascii_lowercase, 6))
print(userLogin)

userPass = ''.join(random.sample(string.ascii_letters + string.punctuation, 8))
print(userPass)

check = True
checkDigit = 0
checkLower = 0
checkUpper = 0
checkPunkt = 0
for s in userPass:
    if s.isdigit():
        checkDigit = True
    elif s.islower():
        checkLower = True
    elif s.isupper():
        checkUpper = True
    elif s in string.punctuation:
        checkDPunkt = True

if checkDigit and checkUpper and checkLower and checkPunkt:
    print("Pass is OK")
else:
    print("Pass is bad")
print(checkDigit)
print(checkLower)
print(checkUpper)
print(checkPunkt)

# myStr = "python was created in the late 1980's python by Guido van Rossum."
# str = myStr.replace(' ', '')
# print(str)
# reverse = str[::-1]
# if str[::1] == reverse:
#     print(str, "is palindrome ")
# else:
#     print("No")

num = '123fnbsd128734837'
# print(list(filter(str.isdigit, num)))
# m = []
# for s in num:
#      if s.isdigit():
#          m.append(int(s))
# print(m)