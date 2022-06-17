"""
3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

file = open("3.txt","r", encoding="utf-8")

salary = {}
low_salary = {}
summ = 0
average = 0

for line in file:
    name, value = line.split()
    salary[name] = float(value)
for name, value in salary.items():
    if value < 20000:
        low_salary[name]=value
for  i, value in enumerate(salary.values(), start=1):
    summ = summ + value
    average = summ/i

print(f"Оклад меньше 20к - {low_salary}")
print(f"Средний доход всех сотрудников: {round(average, 2)}")



