"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""

x = int(input("Введите число: "))
y = int(input("Введите степень отрицательного возведения: "))


def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    result = 1 / result
    return result


print(f"Результат возведения: {round(my_func(x, y), 7)}")
