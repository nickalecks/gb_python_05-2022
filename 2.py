a=0
a=int(input('Введите секунды '))
c=a//3600
m=a%3600
m=m//60
s=a%60
print (f'{c}:{m}:{s}')