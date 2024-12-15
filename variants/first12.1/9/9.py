k = 0
for list in open('9.txt').readlines():
    a = [int(x) for x in list.split()]
    np = [x for x in a if a.count(x) == 1]
    np.sort()
    if len(np) == 5:
        if 3 * (np[0] + np[-1]) <= 2 * (np[1] + np[2] + np[3]):
            k += 1
print(k)
