number = int(input('Если хотите выйти, введите 0. Введите элемент рейтинга: '))
my_list = [7, 5, 3, 3, 2]
while number != 0:
    my_list.append(number)
    my_list.sort()
    my_list.reverse()
    print(my_list)
    number = int(input('Если хотите выйти, введите 0. Введите элемент рейтинга: '))