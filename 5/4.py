"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

file = open("4.txt", "r", encoding="utf-8")
file_new =  open("4_new.txt", "w", encoding="utf-8")

rus = {"One" : "Один", "Two" : "Два" , "Three" : "Три" , "Four" : "Четыре" , "Five" : "Пять" , "Six" : "Шесть" ,
       "Seven" : "Семь" , "Eight" : "Восемь" , "Nine" : "Девять" , "Ten" : "Десять"}


while True:
    data = file.readline()
    for word in data.split():
        if word in rus.keys():
            translate = rus[word] + " "
        else:
            translate = translate + word + " "
    file_new.write(translate + "\n")
    if not data:
        break

file.close()
file_new.close()
#удаление последней строки, так как она дублируется при последнем проходе - проверке на конец файла
file_new =  open("4_new.txt", "r", encoding="utf-8")
data = file_new.readlines()
data = data[:-1]
file_new.close()
file_new = open("4_new.txt", "w", encoding="utf-8")
for word in data:
    file_new.write(word)
file_new.close()



"""           не совсем правильно, так как выводит в одну строку
while True:
    data = file.readline()
    for word in data.split():
        if word in rus.keys():
            file_new.write(rus[word] + " ")
        else:
            file_new.write(word + " ")
    if not data:
        break

file.close()
file_new.close()
"""