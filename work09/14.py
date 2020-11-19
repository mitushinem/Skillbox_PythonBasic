# string = input('Введите текст').split()
# print(f'В строке {len(string)} слов')

string = input('Введите текст').strip()
word = 1
for s in string:
    if s == ' ':
        word += 1
print(f'В строке {word} слов')