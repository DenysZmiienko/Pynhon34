# Задание 1
# Создайте класс Дробь. Используя перегрузку операторов реализуйте
# для него арифметические операции для работы с дробями (операции +, -, *, /).
# Также операторы составного присваивания и методы преобразования (int,float,str)

class Fraction:
    def __init__(self, numerator, denomerator):
        self.numerator = numerator
        self.denomerator = denomerator
        if self.denomerator == 0:
            return ("You can't divide by zero")

    def __str__(self):
        return f"{self.numerator} / {self.denomerator}"

    def __add__(self, other):
        if isinstance(other,Fraction):
            return (self.numerator * other.denomerator + self.denomerator * other.numerator) / (self.denomerator * other.denomerator)
        elif isinstance(other, int):
            return Fraction(self.numerator + other, self.denomerator + other)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return (self.numerator * other.denomerator - self.denomerator * other.numerator) / (self.denomerator * other.denomerator)
        elif isinstance(other, int):
            return Fraction(self.numerator - other, self.denomerator - other)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return (self.numerator * other.numerator / self.denomerator * other.denomerator)
        elif isinstance(other, int):
            return Fraction(self.numerator * other, self.denomerator * other)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return (self.numerator * other.denomerator /  self.denomerator * other.numerator)
        elif isinstance(other, int):
            return Fraction(self.numerator / other, self.denomerator / other)

    def __int__(self):
        return Fraction(int(self.numerator), int(self.denomerator))

    def __float__(self):
        return Fraction(float(self.numerator), float(self.denomerator))

f1 = Fraction(1, 2)
f2 = Fraction(2, 3)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(f1.__float__())

# Задание 2
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
#  Проверка на равенство площадей квартир (операция ==);
#  Проверка на неравенство площадей квартир (операция !=);
#  Сравнение двух квартир по цене (операции > < <= >=).



# Задание 3
# Создать простой калькулятор, используя полиморфизм для выполнения арифметических операций над числами.
# Инструкции:
# Создайте базовый класс Operation, который будет представлять арифметическую операцию. Определите в нем метод perform,
# который будет выполнять операцию(в данном классе без реализации)
# Создайте подклассы Addition, Subtraction, Multiplication и Division, представляющие соответственно сложение, вычитание,
# умножение и деление. Эти классы должны наследовать от Operation и реализовывать метод perform для выполнения своей операции.
# Создайте класс Calculator, который будет принимать два операнда и объект операции (например, Addition, Subtraction,
# и так далее). Класс Calculator должен иметь метод calculate, который будет вызывать метод perform у переданного объекта
# операции для выполнения арифметической операции.
# Создайте экземпляры разных операций (например, Addition, Subtraction, и так далее) и используйте их с объектом Calculator,
# чтобы выполнить различные арифметические операции. Выведите результаты операций на экран.