"""
5. Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""

class Stationery:

     title = '"Ручки и штучки"TM'

     def draw(self):
         print(self.title)
         print('«Запуск отрисовки»')

class Pen(Stationery):
    def draw(self):
        print(self.title)
        print('Пишем ручкой.')


class Pencil(Stationery):
    def draw(self):
        print(self.title)
        print('Пишем карандашём.')

class Handle(Stationery):
    def draw(self):
        print(self.title)
        print('Пишем маркером.')

a = Stationery()
b = Pen()
c = Pencil()
d = Handle()
a.draw()
b.draw()
c.draw()
d.draw()