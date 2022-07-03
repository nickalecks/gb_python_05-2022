"""
4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print('Машина тронулась.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print(f'Машина повернула {direction}.')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}км/ч.')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            x = self.speed - 60
            print(f'Превышение скорости на {x}км/ч.')
        else:
            print(f'Текущая скорость {self.speed}км/ч.')

class SportCar(Car):

    def show_speed(self):
        if self.color == 'Red' or self.color == 'red' :
            print('Red goes Fasta!')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            x = self.speed - 40
            print(f'Превышение скорости на {x}км/ч.')
        else:
            print(f'Текущая скорость {self.speed}км/ч.')

class PoliceCar(Car):

    def police(self):
        if self.is_police == True:
            print('Полицейское авто.')
        else:
            print('Не из полиции.')

Volga = Car(40, 'Green', 'Volga', 0)
Audi = PoliceCar(70, 'Police', 'Audi', 1)
SportCar = SportCar(120, 'Red', 'VAZ-2101', 0)
WorkCar = WorkCar(50, 'Yellow', 'KIA', 0)
TownCar = TownCar(55, 'Black', 'Pobeda', 0)

Volga.go()
Volga.turn('на лево')
Audi.police()
SportCar.show_speed()
WorkCar.show_speed()
TownCar.show_speed()