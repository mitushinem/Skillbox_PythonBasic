ad_lenght = int(input('Введите общую длину колонтитула в символах: '))
nubmer_mask = int(input('Введите количество восклицательных знаков: '))

result = ad_lenght - nubmer_mask
if result % 2 == 0:
    print("~" * (result//2) + nubmer_mask * "!" + "~" * (result//2))
else:
    print("~" * (result//2) + nubmer_mask * "!" + "~" * (result//2 - 1))