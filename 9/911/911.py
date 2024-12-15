k = 0
for list in open('911.txt').readlines():
    a = [int(x) for x in list.split()]
    p3 = [x for x in a if a.count(x) == 3]
    np = [x for x in a if a.count(x) == 1]
    if len(p3) == 3 and len(np) == 3:
        if sum(p3) ** 2 > sum(np) ** 2:
            k += 1
print(k)