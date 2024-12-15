
k = 0
for list in open('9.txt'):
    a = [int(x) for x in list.split()]
    p3 = [x for x in a if x == 60 and a.count(x) == 3]
    if len(p3) != 0:
        k += 1
print(k)