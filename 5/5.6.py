k = []
for n in range(1, 100):
    s = bin(n)[2:]
    if int(s, 2) % 5 == 0:
        s = s[0] + s[1] + s[2] + s
    else:
        b = int(s, 2) % 5 * 5
        b = bin(b)[2:]
        s += b
    if int(s, 2) < 313:
        k.append(n - 1)
print(k)
