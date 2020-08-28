earnings = int(input('Введите выручку: '))
expenses = int(input('Введите издержки: '))
profit = earnings - expenses
eff = profit / earnings
if profit > 0:
    print('У вас прибыль: выручка больше издержек')
    print('Рентабельность выручки: ', eff)
    staff = int(input('Введите численность чотрудников: '))
    print('Прибыль фирмы в расчете на 1 сотрудника: ', profit / staff)
elif profit == 0:
    print('Прибыль равна нулю')
else:
    print('У вас убыток: издержки больше выручки')
