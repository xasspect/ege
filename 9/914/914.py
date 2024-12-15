k = 0
for list in open('914.txt').readlines():
    a = [int(x) for x in list.split()]
    np = [x for x in a if a.count(x) == 1]
    np.sort()
    if len(np) == 5:
        if (np[-1] + np[0]) * 2 >= sum(np[1:4]):
            k += 1
print(k)

