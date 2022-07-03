"""
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).
"""

accounting = {'Office': {'Printer': 0, 'Scanner': 0, 'Xerox': 0},
              'Warehouse': {'Printer': 0, 'Scanner': 0, 'Xerox': 0}}

class Warehouse_for_office():

    def __init__(self):
        self.accounting = accounting

    def journal(self):

        name = input('Введите наименование поступившей техники \n (Printer , Scanner или Xerox) : ')
        number = int(input('Введите количество: '))
        if name == 'Printer':
            a = self.accounting['Warehouse']['Printer']
            a += number
            self.accounting['Warehouse']['Printer'] = a
            return self.accounting
        elif name == 'Scanner':
            a = self.accounting['Warehouse']['Scanner']
            a += number
            self.accounting['Warehouse']['Scanner'] = a
            return self.accounting
        elif name == 'Xerox':
            a = self.accounting['Warehouse']['Xerox']
            a += number
            self.accounting['Warehouse']['Xerox'] = a
            return self.accounting

    @staticmethod
    def move():

        name = input('Введите наименование перевозимой техники \n (Printer , Scanner или Xerox) : ')
        destination = input('Куда везём? \n (Warehouse, Office) : ')
        number = int(input('Введите количество: '))
        # Со склада
        if destination == 'Office':
            if name == 'Printer':
                a = accounting['Warehouse']['Printer']
                a -= number
                if a < 0:
                    print(f'На складе осталось только {number + a}.')
                    return accounting
                else:
                    accounting['Warehouse']['Printer'] = a
                    a = accounting['Office']['Printer']
                    a += number
                    accounting['Office']['Printer'] = a
                    return accounting
            elif name == 'Scanner':
                a = accounting['Warehouse']['Scanner']
                a -= number
                if a < 0:
                    print(f'На складе осталось только {number + a}.')
                    return accounting
                else:
                    accounting['Warehouse']['Scanner'] = a
                    a = accounting['Office']['Scanner']
                    a += number
                    accounting['Office']['Scanner'] = a
                    return accounting
            elif name == 'Xerox':
                a = accounting['Warehouse']['Xerox']
                a -= number
                if a < 0:
                    print(f'На складе осталось только {number + a}.')
                    return accounting
                else:
                    accounting['Warehouse']['Xerox'] = a
                    a = accounting['Office']['Xerox']
                    a += number
                    accounting['Office']['Xerox'] = a
                    return accounting
        # Из офиса
        if destination == 'Warehouse':
            if name == 'Printer':
                a = accounting['Office']['Printer']
                a -= number
                if a < 0:
                    print(f'В офисе осталось только {number + a}.')
                    return accounting
                else:
                    accounting['Office']['Printer'] = a
                    a = accounting['Warehouse']['Printer']
                    a += number
                    accounting['Warehouse']['Printer'] = a
                    return accounting
            elif name == 'Scanner':
                a = accounting['Office']['Scanner']
                a -= number
                if a < 0:
                    print(f'В офисе осталось только {number + a}.')
                    return accounting
                else:
                    accounting['Office']['Scanner'] = a
                    a = accounting['Warehouse']['Scanner']
                    a += number
                    accounting['Warehouse']['Scanner'] = a
                    return accounting
            elif name == 'Xerox':
                a = accounting['Office']['Xerox']
                a -= number
                if a < 0:
                    print(f'В офисе осталось только {number + a}.')
                    return accounting
                else:
                    accounting['Office']['Xerox'] = a
                    a = accounting['Warehouse']['Xerox']
                    a += number
                    accounting['Warehouse']['Xerox'] = a
                    return accounting


x = Warehouse_for_office()
print(x.journal())
print(x.move())
