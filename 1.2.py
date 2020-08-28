time = int(input('Введите время в секундах: '))
hh = time // 3600
min = (time - hh * 3600) // 60
sec = (time % 3600) % 60
print(f" {hh} : {min} : {sec}")
