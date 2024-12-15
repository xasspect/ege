k = 0
for list in open('9.txt'):
    a = [int(x) for x in list.split()]
    a.sort()
    p2 = [x for x in a if a.count(x) == 2]

    if len(p2) != 0:
        if a[-1] < (a[0] + a[1] + a[2]):
            k += 1
print(k)