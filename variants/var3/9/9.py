k = 0
for list in open('9.txt'):
    a = [int(x) for x in list.split()]
    a.sort()
    if (a[0] + a[-1]) ** 2 > (a[1] ** 2) + (a[2] ** 2) + (a[3] ** 2):
        k += 1
print(k)
