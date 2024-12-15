a = [int(x) for x in open('26.txt')]
a = sorted(a)[::-1]

r = 0
u = []
for i in range(len(a)):
    k = 0
    y = []
    for j in range(len(a)):
        if a[i] - a[j] == 8:
            i = j
            k += 1
            y.append(a[j])
    r = max(r, k)
    print(y)
    if len(u) < len(y):

        u = y
print(r, u, len(u))