a = list(map(int, open('17.txt')))
s = max([x for x in a if len(str(abs(x))) == 2])

t = 0
r = []
for x in range(len(a) - 1):
    if str(a[x])[0] != '-' and len(str(abs(a[x]))) == 3 or str(a[x + 1])[0] != '-' and len(str(abs(a[x + 1]))) == 3:
        if (a[x] + a[x + 1]) % 98 == 0:
            t += 1
            r.append(a[x] + a[x + 1])
print(t, max(r))
