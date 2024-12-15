k = 0
for i in open('91.txt'):
    a = [int(x) for x in i.split()]
    s = [int(x) for x in sorted(a)[::-1]]
    if min(a) > 10:
        if a[0] ** 3 > (2 * a[1]) * (2 * a[2]) * (2 * a[3]):
            k += 1
print(k)

