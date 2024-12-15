k = 0
for list in open('98.txt').readlines():
    a = [int(x) for x in list.split()]
    np = [x for x in a if a.count(x) == 1]
    np.sort()

    p2 = [x for x in a if a.count(x) == 2]
    if len(p2) == 2 and len(np) == 5:
        if p2[0] ** 2 < np[0] * np[1] * np[2]:
            k += 1
print(k)
