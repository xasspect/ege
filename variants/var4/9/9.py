k = 0
for list in open('9.txt'):
    a = [int(x) for x in list.split()]
    a.sort()
    if (a[0] + a[-1]) % 3 == 0:

        if a[0] - a[1] == a[2] - a[3] or a[3] - a[2] == a[1] - a[0] or a[3] - a[2] == a[0] - a[1] or a[2] - a[3] == a[1] - a[0]:
            k += 1
        elif a[0] - a[2] == a[1] - a[3] or a[0] - a[2] == a[3] - a[1] or a[2] - a[0] == a[1] - a[3] or a[2] - a[0] == a[3] - a[1]:
            k += 1
        elif a[0] - a[3] == a[1] - a[2]:
            k += 1


print(k)