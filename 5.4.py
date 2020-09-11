my_trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_file = []

with open("text54.txt", encoding="Utf-8") as file:
    for i in file:
        i = i.split(' ', 1)
        my_file.append(my_trans[i[0]] + ' ' + i[1])
    print(my_file)

with open("transl_text54.txt",'w', encoding="utf-8") as trans:
    trans.writelines(my_file)


