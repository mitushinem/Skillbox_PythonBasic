x = int(input('Дано число X: '))
step1, step2, result_x1, result_x2 = 0, 1, 1, 1
for _ in range(6):
    step1 = step1 * 2 + 1
    step2 = step2 * 2
    result_x1 *= (x - step1)
    result_x2 *= (x - step2)
print(result_x1/result_x2)