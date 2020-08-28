number = int(input('Введите целое положительно число: '))
max_number = number % 10
new_number = number // 10
while new_number > 0:
    if new_number % 10 > max_number:
        max_number = new_number % 10
    new_number = new_number // 10
print(max_number)
