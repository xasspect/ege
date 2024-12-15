k = 0
for list in open('912.txt'):
    b = []
    d = []
    a = [int(x) for x in list.split()]
    for x in a:
        if str(x)[-1] == '5':
            b.append(x)
        else:
            d.append(x)
    if len(b) >= 2 and len(b) + len(d) == 5:
        b = b + d
        b.sort()
        if (a[-1] + a[-2]) * 2 > (a[0] + a[1] + a[2]) * 3:
            k += 1
print(k)


