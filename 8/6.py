"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""

accounting = {'Office': {'Printer': 0, 'Scanner': 0, 'Xerox': 0},
              'Warehouse': {'Printer': 0, 'Scanner': 0, 'Xerox': 0}}

def GetNumber():
    while type:
        number = input('Введите число: ')
        try:
            number = int(number)
        except ValueError:
            print('"' + number + '"' + ' - не является числом')
        else:
            break
    return abs(number)

def GetName():

    x = 1
    while x == 1:
        name = input('Введите наименование поступившей техники или его номер \n 1)Printer 2)Scanner 3)Xerox : ')
        if name == 'Printer' or name == 'Scanner' or name == 'Xerox' or name == '1' or name == '2' or name == '3':
            x = 0
            if name == '1':
                name = 'Printer'
            elif name == '2':
                name = 'Scanner'
            elif name == '3':
                name = 'Xerox'
            print(name)
        else:
            print('Введена неверная информация.')
    return name


class Warehouse_for_office():


    def __init__(self):
        self.accounting = accounting

    @staticmethod
    def journal():

        name = GetName()
        number = GetNumber()

        if name == 'Printer':
            a = accounting['Warehouse']['Printer']
            a += number
            accounting['Warehouse']['Printer'] = a
            return accounting
        elif name == 'Scanner':
            a = accounting['Warehouse']['Scanner']
            a += number
            accounting['Warehouse']['Scanner'] = a
            return accounting
        elif name == 'Xerox':
            a = accounting['Warehouse']['Xerox']
            a += number
            accounting['Warehouse']['Xerox'] = a
            return accounting



x = Warehouse_for_office()
print(x.journal())