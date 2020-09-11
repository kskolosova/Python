my_list = []
while True:
    line = input('Введите текст: ')
    if line == '':
        print(my_list)
        exit()
    else:
        new_line = line + '\n'
        my_list.append(new_line)

    with open("text51.txt", "w") as f:
        f.writelines(my_list)
