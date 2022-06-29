"""
2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

class Abstract_Clothing(ABC):

    def __init__(self, V, H):
        self.V = V
        self.H = H

    def Abstract_Test(self):
        print('Я не придумал, что можно наследовать в данном примере.')

    def Size(self):
        pass
    def Growth(self):
        pass

    @property
    def Summ(self):
        sum = S + G
        return f'Общие затраты - {round(sum, 2)}'


class Coat(Abstract_Clothing):
    @property
    def Size(self):
        global S
        S = (self.V / 6.5 + 0.5)
        return f'Затраты на пальто - {round(S, 2)}'


class Suit(Abstract_Clothing):
    @property
    def Growth(self):
        global G
        G = (2*self.H + 0.3)
        return f'Затраты на костюм - {G}'



cl = Abstract_Clothing(5,5)
c = Coat(5,5)
s = Suit(5,5)
print(c.Size)
print(s.Growth)
print(cl.Summ)
s.Abstract_Test()

