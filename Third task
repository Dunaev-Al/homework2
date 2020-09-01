seasons_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
seasons_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

user_season =int(input('Введите номер месяца: '))

if user_season <= 12:
    if user_season <= 2 or user_season == 12:
        print('Зима')
    elif user_season <= 5:
        print('Весна')
    elif user_season <= 8:
        print('Лето')
    else:
        print('Осень')
else:
    print('Месяцев так то 12...')

for key in seasons_dict.keys():
    if user_season in seasons_dict[key]:
        print(key)
