with open('text52.txt', encoding='Utf-8') as file:
    lines = 0
    for line in file:
        lines += 1

        i = 0
        word = 0
        for j in line:
            if j != ' ' and i == 0:
                word += 1
                i = 1
            elif j == ' ':
                i = 0

        print(line, word, 'слов.')


print(f'Всего строк: {lines}')
