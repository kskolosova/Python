def my_sum():
    sum_result = 0
    ext = False
    while not ext:
        numbers = input('Введите числа через пробел или нажмите Q для выхода: ').split()

        result = 0
        for i in range(len(numbers)):
            if numbers[i] == 'q' or numbers[i] == 'Q':
                ext = True
                break
            else:
                result += int(numbers[i])
        sum_result += result
        print(f'Текущая сумма: {sum_result}')
    print(f'Финальная сумма: {sum_result}')


my_sum()
