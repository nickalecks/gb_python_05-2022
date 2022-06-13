# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    if a <= b and a <= c:
        return b + c
    elif b <= c:
        return a + c
    else:
        return a + b

a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))

my_sum = my_func(a, b, c)
print('Сумму наибольших двух чисел', my_sum)
