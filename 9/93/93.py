count = 0
for list in open('93.txt').readlines():
    a = [int(x) for x in list.split()]
    p1 = [x for x in a if a.count(x) == 2]
    np = [x for x in a if a.count(x) == 1]

    if len(p1) == 2 and len(np) == 2:
        if p1[0] % 2 == 0:
            if np[0] % 2 != 0 and np[1] % 2 != 0:
                count += 1
print(count)

