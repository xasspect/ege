count = 0
for list in open('91.txt').readlines():
    a = [int(x) for x in list.split()]
    p3 = [x for x in a if a.count(x) == 3]
    np = [x for x in a if a.count(x) == 1]
    print(p3)
    if len(p3) == 3 and len(np) == 3:
        if sum(p3) ** 2 > sum(np) ** 2:
            count += 1
print(count)