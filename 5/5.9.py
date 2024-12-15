k = []
for n in range(1, 100):
    s = bin(n)[2:]
    if int(s, 2) % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'

    r = int(s, 2)
    if r > 516:
        k.append(n)
print(min(k))
