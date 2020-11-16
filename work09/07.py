message = input('Введите текст: ')

for s in message:
    if not s == '*':
        print(s, end='')