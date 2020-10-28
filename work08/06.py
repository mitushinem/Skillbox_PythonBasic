
n = int(input('Сколько лет было дереву: '))
k = int(input('С какой периодичностью Алена будет сажать новое дерево: '))
summ = 0
for value in range(6, n + 1, k):
    user_data = int(input('Сколько посадить деревьев? '))
    summ += user_data
print(f'Будет посажено {summ} деревьев')


