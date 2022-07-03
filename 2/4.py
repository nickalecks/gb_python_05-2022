a=input('Введите несколько слов, разделённых пробелами: ').split()
for ind, i in enumerate(a, 1):
    print(ind, i[0:10])
print(type(a))