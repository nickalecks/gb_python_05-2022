"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(a, b, c):
    numbers = [a, b, c]
    max_seq = []
    max_1 = max(numbers)
    max_seq.append(max_1)
    numbers.remove(max_1)
    max_2 = max(numbers)
    max_seq.append(max_2)
    s=sum(max_seq)
    return s
print("Сумма двух максимальных элементов равна ", my_func(int(input('Введите первое число: ')),int(input('Введите второе число: ')),
int(input('Введите первое число: '))))

