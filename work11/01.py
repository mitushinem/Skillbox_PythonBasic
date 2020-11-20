cost = float(input('Введите стоимость покупки, в евро: '))

dollar = 60.87
euro = 1.25

result = round((cost * euro * dollar), 2)
print('Стоимость в рублях: ', result)

