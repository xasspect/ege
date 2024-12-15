k = 0
for list in open('9.txt'):
    a = [int(x) for x in list.split()]
    p9 = [x for x in a if a.count(90) == 1]
    p9.sort()

    if len(p9) > 0 and p9[-1] == 90:
        if p9[0] + p9[1] == 90:
            k += 1
print(k)