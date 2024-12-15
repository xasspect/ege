count = 0
for list in open('92.txt').readlines():
    a = [int(x) for x in list.split()]
    if a[0] + a[1] == a[2] + a[3] or a[0] + a[2] == a[1] + a[3] \
        or a[0] + a[3] == a[1] + a[2]:
        if sorted(a)[-1] < sum(sorted(a)[:-1]):
            count += 1
print(count)

