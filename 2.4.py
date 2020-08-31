user_line = input('Введите строку из нескольких слов: ').split()
for words in user_line:
    if len(words) > 10:
        print(words[0:10])
    else:
        print(words)
