"""
6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

file = open("6.txt", "r", encoding="utf-8")

sorted = open("6_new.txt", "w", encoding="utf-8")

result = {}
while True:
    data = file.readlines()
    for line in data:
        line = line.replace("(л)", "")
        line = line.replace("(пр)", "")
        line = line.replace("(лаб)", "")
        line = line.replace("—", "")
        line = line.replace(".", "")
        line = line.replace(":", "")
        sorted.write(line)
    if not data:
        break
file.close()
sorted.close()

sorted = open("6_new.txt", "r", encoding="utf-8")

while True:
    data = sorted.readline()
    s = 0
    line = data.split()
    for x in line[1:]:
        s += int(x)
        result[line[0]] = s
    if not data:
        break
print(result)

sorted.close()