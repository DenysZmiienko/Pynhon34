import random

#
# class Student:
#     special = "Computer"
#     def __init__(self,name,age,group,email,phone):
#
#         self.__name = name
#         self.age = age
#         self.group = group
#         self.email = email
#         self.__phone = phone
#
#         self.__st_id = random.randint(1,100)
#
#     def __del__(self):
#         print("del st")
#     def showInfo(self):
#         return f"Student: {self.name} , {self.age} , {self.group} , {self.email} , {self.__phone}"
#
#     def __getId(self):
#         return f"{self.__st_id}"
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self,new_name):
#         self.name = new_name
#
#     def get_phone(self):
#         return self.__phone
#
#     def set_phone(self, new_phone):
#         self.__phone = new_phone
#
# student1 = Student('Bob', 26, "Python34", "Zm34@mail", "123456")
# student2 = Student('Nik', 19, "Python35", "Zm36@mail", "654321")
# student1.set_name("Mark")
# student1.set_phone("33333")
# print(student1.get_name())
# print(student1.showInfo())
# print(student2.showInfo())

# class Student:
#     # public prop
#     spec = "Computer"
#
#     def __init__(self, name, age):
#         print("creating new st")
#         # public prop
#         self.__name = name
#         self.age = age
#         # private prop
#         self.__st_id = random.randint(1, 100)
#
#     def __del__(self):
#         print("del st")
#
#     def showInfo(self):
#         return f"Student: {self.__name} is {self.age} years old!"
#
#     def __getId(self):
#         return f"{self.__st_id}"
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#
# st1 = Student('Bob', 26)
# st2 = Student("Nick", 19)
#
# # st1.name = "Anna"
# # print(st1.__st_id)  # no
# st1.name = "qwerty"
#
# st1.newprop = "test"
# print(st1.newprop)
# # print(st1.get_name())
# print(st1.showInfo())
# print(st2.showInfo())


class People():
    def __init__(self, full_name, bithtday, country, city, phone ):
        print("creating new st")
        self.full_name = full_name
        self.bithtday = bithtday
        self.country = country
        self.city = city
        self.phone = phone
    def __del__(self):
        print("del People")
    def showInfo(self):
        return f"People: {self.full_name}, bithtday:  {self.bithtday}, country: {self.country}, city: {self.city}, phone: {self.phone} "
    def get_bithtday(self):
        if self.bithtday > 18:
            return True
        else:
            return False

    @property
    def full_name(self):
        return self.full_name

    @full_name.setter
    def name(self, new_full_name):
        self.full_name = new_full_name
people1 = People('Full Bob St', 26, "USA", "Florida", "123456")
print(people1.showInfo())