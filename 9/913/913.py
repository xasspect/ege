k = 0
for list in open('913.txt'):
    a = [int(x) for x in list.split()]
    p2 = [x for x in a if a.count(x) == 2 and x % 2 == 0]
    np = [x for x in a if a.count(x) == 1 and x % 2 == 1]
    if len(p2) == 2 and len(np) == 2:
        k += 1
print(k)