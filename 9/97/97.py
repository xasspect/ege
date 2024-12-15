k = 0
for list in open('97.txt').readlines():
    a = [int(x) for x in list.split()]
    p2 = [x for x in a if a.count(x) == 2]
    np = [x for x in a if a.count(x) == 1]
    print(np, p2)
    a.sort()
    if len(np) == 2 and len(p2) == 2:

        if a[-1] < (a[0] + a[1] + a[2]):
            k += 1
print(k)