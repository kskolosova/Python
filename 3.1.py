def my_division():
    try:
        x = int(input('Введите делимое: '))
        y = int(input('Введите делитель: '))
        z = x / y
    except ZeroDivisionError:
        return 'Делить на 0 нельзя'
    except ValueError:
        return 'Можно вводить только числа'

    return z


print(f'Частное =  {my_division()}')
