a = list(map(int, open('1711.txt')))
k = max([x for x in a if str(x)[-2:] == '68'])

s = 0
r = []
for x in range(len(a) - 3):
    x1 = len(str(abs(a[x])))
    x2 = len(str(abs(a[x + 1])))
    x3 = len(str(abs(a[x + 2])))
    x4 = len(str(abs(a[x + 3])))
    if a[x] + a[x + 1] + a[x + 2] + a[x + 3] >= k:

        if (x1 == 2 and x2 != 2 and x3 != 2 and x4 != 2):
            s += 1
            r.append(a[x] + a[x + 1] + a[x + 2] + a[x + 3])
        elif (x1 != 2 and x2 == 2 and x3 != 2 and x4 != 2):
            s += 1
            r.append(a[x] + a[x + 1] + a[x + 2] + a[x + 3])
        elif (x1 != 2 and x2 != 2 and x3 == 2 and x4 != 2):
            s += 1
            r.append(a[x] + a[x + 1] + a[x + 2] + a[x + 3])
        elif (x1 != 2 and x2 != 2 and x3 != 2 and x4 == 2):
            s += 1
            r.append(a[x] + a[x + 1] + a[x + 2] + a[x + 3])
        elif (x1 == 2 and x2 == 2 and x3 == 2 and x4 == 2):
            s += 1
            r.append(a[x] + a[x + 1] + a[x + 2] + a[x + 3])
print(s, max(r))



