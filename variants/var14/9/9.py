
k = 0
for list in open('9.txt'):
    a = [int(x) for x in list.split()]
    pc2 = [x for x in a if x % 2 == 0]
    pn2 = [x for x in a if x % 2 != 0]
    if len(pc2) == 6:
        k += 1
    if len(pn2) == 6:
        k += 1
print(k)