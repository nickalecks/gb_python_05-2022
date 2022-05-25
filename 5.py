a=int(input('Рейтинг(натуральное число): '))
list=[7,5,3,3,2]
max=max(list)
min=min(list)
len=len(list)
if a>max:
    list.insert(0,a)
elif a<min:
    list.insert(len,a)
elif a in list:
    list.insert(list.index(a),a)
else:
    list.append(a)
print(list)


