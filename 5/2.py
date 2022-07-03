"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
"""

file = open("2.txt", "r", encoding="utf-8")

words_count = 0
while True:
    content = file.readlines()
    for i,line in enumerate(content, start=1):
        for x, words in enumerate(line.split(), start=1):
            i  #костыль, чтобы работал enumerate
        words_count = words_count + x
    if not content:
        break
print(f"В файле 2.txt {words_count} слов.")
print(f"В файле 2.txt {i} строки.")

file.close()