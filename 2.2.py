sum_content = int(input('Введите количество элементов списка: '))
my_list = []
i = 0
content = 0
while i < sum_content:
    my_list.append(input('Введите элемент списка: '))
    i += 1
for element in range(int(len(my_list)/2)):
    my_list[content], my_list[content + 1] = my_list[content + 1], my_list[content]
    content += 2
print(my_list)
