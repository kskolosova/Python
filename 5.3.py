summa = 0
count = 0
under_rate = []
with open("text53.txt", encoding='Utf-8') as file:
    for line in file:
        print(line, end='')
        salary = line.split()
        if float(salary[1]) <= 20000:
            under_rate.append(salary[0])
        summa += float(salary[1])
        count += 1
result = summa / count
print(f'Cотрудники у кого зп ниже 20 тысяч: {under_rate}')
print(round(result,2))


