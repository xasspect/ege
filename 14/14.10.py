k = []
t = 5 ** 2025 + 5 ** 400
for x in range(10, 100):
    s = t - x
    while s:
        if s % 5 == 0:
            if str(s).count('4') > 0:
                k += [s]
        s //= 5
t = max(k)
for i in range(len(k) - 1):
    if k[i] == t:
        print(i + 1)