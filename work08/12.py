x = int(input('Дано число X: '))
numerator, denominator = 1, 1
for i in range(1, 7):
    numerator *= (x - (i**2 - 1))
    denominator *= (x - i**2)
print(numerator/denominator)


