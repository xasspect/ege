k = 0
for list in open('99.txt').readlines():
    a = [int(x) for x in list.split()]
    a.sort()
    if a[-1] < a[0] + a[1] + a[2]:
        if a[0] + a[1] == a[2] + a[3] or a[0] + a[2] == a[1] + a[3] or a[0] + a[3] == a[1] + a[2]:
            k += 1
print(k)


