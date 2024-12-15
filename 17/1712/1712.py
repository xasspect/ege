a = list(map(int, open('1712.txt')))
y = int(min([str(x) for x in a if len(str(abs(x))) == 2]))
u = max([x for x in a if len(str(abs(x))) == 4 and str(abs(x))[-1] == '1'])
s = 0
r = []
for x in range(len(a) - 2):
    t = y ** 2
    x1 = a[x]
    x2 = a[x + 1]
    x3 = a[x + 2]

    if (x1 > t and x2 > t and x3 <= t):
        if abs(x1) * abs(x2) * abs(x3) % u == 0:
            s += 1
            r.append(abs(x1) + abs(x2) + abs(x3))
    elif (x2 > t and x3 > t and x1 <=t):
        if abs(x1) * abs(x2) * abs(x3) % u == 0:
            s += 1
            r.append(abs(x1) + abs(x2) + abs(x3))
    elif (x1 > t and x3 > t and x2 <=t):
        if abs(x1) * abs(x2) * abs(x3) % u == 0:
            s += 1
            r.append(abs(x1) + abs(x2) + abs(x3))






print(s, r)

