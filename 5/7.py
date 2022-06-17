"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

firms = {}
average = {}
sum = 0
result = []
a = 0

import json

with open("7.txt") as file:
    for line in file:
        name, form, receipts, cost = line.split()
        firms[name] = int(receipts) - int(cost)

    for value in firms.values():
        if int(value) > 0:
            a = a+1
            sum = sum + value
            average["average_profit"] = round(sum / a, 2)

result.append(firms)
result.append(average)

with open("result.json", "w") as data:
    json.dump(result, data)

print(result)
