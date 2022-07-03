"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных
"""

class Data():

    def __init__(self,data):
        self.data = data

    @classmethod
    def new_data(cls, data):
        for i in data.split('-'):
            day, month, year = data.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        print(f'{day:02d} {month:02d} {year}')
        return day, month, year



    @staticmethod
    def validator(day, month, year):
        if day in range(1,32):
            print('Day - ok')
        else:
            print('Day - Error')
        if month in range(1, 13):
            print('Month - ok')
        else:
            print('Month - Error')
        if year in range(-4000, 3000):
            print('Year - ok')
        else:
            print('Year - Error')


d = Data.new_data('15-02-1999')
Data.validator(d[0],d[1],d[2])

