"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
"""

class Warehouse_for_office():

    def __init__(self, param):
        self.param = param

class office_equipment():

    def __init__(self, model, cost, quantity):
        self.model = model
        self.cost = cost
        self.quantity = quantity

class Printer(office_equipment):

    def __init__(self, model, cost, quantity, color, resolution):
        super().__init__(model, cost, quantity)
        self.color = color
        self.resolution = resolution

class Scanner(office_equipment):

    def __init__(self, model, cost, quantity, color_depth, max_resolution):
        super().__init__(model, cost, quantity)
        self.color_depth = color_depth
        self.max_resolution = max_resolution

class Xerox(office_equipment):

    def __init__(self, model, cost, quantity, speed, technology):
        super().__init__(model, cost, quantity)
        self.speed = speed
        self.technology = technology