season_list = ['winter', 'spring', 'summer', 'fall']
season_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'fall'}
month = int(input('Введите номер месяца: '))
if month == 1 or month == 2 or month == 12:
    print(season_list[0])
    print(season_dict[1])
elif month == 3 or month == 4 or month == 5:
    print(season_list[1])
    print(season_dict[2])
elif month == 6 or month == 7 or month == 8:
    print(season_list[2])
    print(season_dict[3])
elif month == 9 or month == 10 or month == 11:
    print(season_list[3])
    print(season_dict[4])
else:
    print('Введено неверное значение. В году 12 месяцев')
