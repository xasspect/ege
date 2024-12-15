k = 0
for list in open('9.txt'):
    a = [int(x) for x in list.split()]
    p2 = [x for x in a if a.count(x) == 2]
    if sum(a) == 180:
        if len(p2) == 2:
            k += 1
print(k)