k = 0
for list in open('94.txt').readlines():
    a = [int(x) for x in list.split()]

    a.sort()

    if a[0] + a[-1] < a[1] + a[2]:
        k += 1
print(k)


