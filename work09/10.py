string = input('Введите текст: ').split()
max_len = 0

for s in string:
    if len(s) > max_len:
        max_len = len(s)

print(f'Самое длинное слово состоит из {max_len} символов')