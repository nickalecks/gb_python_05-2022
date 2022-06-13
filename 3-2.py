# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def user_data_to_string(name, surname, year, city, email, phone):
    return ','.join([name, surname, year, city, email, phone])

name = input('Введите имя: ')
surname = input('Введите фамилия: ')
year = int(input('Введите год рождения: '))
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')

result = user_data_to_string(name, surname, year, city, email, phone)

print(result)
