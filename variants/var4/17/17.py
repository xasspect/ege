a = list(map(int, open('17.txt')))


s = 0
r = []
for x in range(len(a) - 1):
    if (a[x] + a[x + 1]) % 3 == 0 and (a[x] + a[x + 1]) % 6 != 0:
        if str(a[x] * a[x + 1])[-1] == '8':
            s += 1
            r.append(a[x] + a[x + 1])

print(s, max(r))

