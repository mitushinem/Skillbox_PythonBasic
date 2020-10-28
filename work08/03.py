
debtor = int(input('Введите количество должников: '))
summ = 0
for value in range(0, debtor, 5):
    print('Должник с номером', value)
    user_data = int(input('Сколько должны?  '))
    summ += user_data
print('Общая сумма долга: ', summ)