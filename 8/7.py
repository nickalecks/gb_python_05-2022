"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
"""

class Complex():

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        self.number = self.number + other
        print(self.number)

    def __mul__(self, other):
        self.number = self.number * other
        print(self.number)

x = Complex(4+2j)
y = 1+2j
x.__add__(y)
x.__mul__(y)


