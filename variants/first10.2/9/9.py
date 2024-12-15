k = 0
for list in open('9.txt').readlines():
    a = [int(x) for x in list.split()]
    p3 = [x for x in a if x % 2 != 0 and a.count(x) == 3]
    np = [x for x in a if x % 2 == 0 and a.count(x) == 1]
    if len(p3) == 3 and len(np) == 1:
        print(p3, np)
        k += 1
print(k)