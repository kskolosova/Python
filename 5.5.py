with open("text55.txt", 'w') as file:
    line = input('Введите числа через пробел: ')
    file.write(line)
    my_count = line.split()
    print(sum(map(int, my_count)))