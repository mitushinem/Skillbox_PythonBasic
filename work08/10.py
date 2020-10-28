
educational_grant = int(input('Ежемесячная стипендия студента составляет руб.: '))
expenses = int(input('Расходы студента составляет руб.: '))

while educational_grant >= expenses:
    print('Хорошо живет)))')
    expenses = int(input('Расходы студента составляет руб.: '))

money_summ = expenses
for month in range(2, 11):
    expenses += expenses * .03
    money_summ += expenses

print('У родителей один раз в начале обучения необходимо получить', round(money_summ))


