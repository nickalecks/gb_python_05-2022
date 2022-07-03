
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

    @staticmethod
    def move():

        name = input('Введите наименование перевозимой техники \n (Printer , Scanner или Xerox) : ')
        destination = input('Куда везём? \n (Warehouse, Office) : ')
        number = int(input('Введите количество: '))
        #Со склада
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
        #Из офиса
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

