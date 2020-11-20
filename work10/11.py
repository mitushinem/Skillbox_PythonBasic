
for n in range(2, 10000):
    tmp_sum = 0
    for i in range(1, n):
        if n % i == 0:
            tmp_sum += i
    if n == tmp_sum:
        print(n, end=' ')