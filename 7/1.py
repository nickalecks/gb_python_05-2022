"""
1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31 22
37 43
51 86
3 5 32
2 4 6
-1 64 -8
3 5 8 3
8 3 7 1
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix():

    def __init__(self, matrix_list):
        self.matrix_list = list(matrix_list.split())

    def __str__(self):
        return f'Матрица вида 2на2: \n{self.matrix_list[0]} {self.matrix_list[1]}\n{self.matrix_list[2]} {self.matrix_list[3]}'

    def __add__(self, other):
        new_matrix = int(self.matrix_list[0]) + int(other.matrix_list[0]),\
                     int(self.matrix_list[1]) + int(other.matrix_list[1]),\
                     int(self.matrix_list[2]) + int(other.matrix_list[2]),\
                     int(self.matrix_list[3]) + int(other.matrix_list[3])
        new_matrix = list(new_matrix)
        return f'Новая матрица вида 2на2: \n{new_matrix[0]} {new_matrix[1]}\n{new_matrix[2]} {new_matrix[3]}'

m1 = Matrix("31 22 37 43")
m2 = Matrix("1 2 3 4")
print(m1)
print(m1+m2)