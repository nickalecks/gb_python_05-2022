"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class OwnError(Exception):

    def __init__(self, txt):
        self.txt = txt

division = 0
input_data = input('Введите  число - делимое: ')
input_data2 = input('Введите  число - делитель: ')

try:

    input_data = int(input_data)
    input_data2 = int(input_data2)
    while input_data2 == 0:
        input_data2 = input('Пытаетесь поделить на 0? Введите другое число: ')
        input_data2 = int(input_data2)

    division = input_data / input_data2
    print(round(division, 2))

except ZeroDivisionError:
    print("На ноль делить нельзя")

except ValueError:
    print('Вы ввели не число.')

except OwnError as error:
    print(error)