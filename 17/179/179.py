a = list(map(int, open('179.txt')))
k = min(set([x for x in a if x % 52 == 0]))

r = []
t = 0
for x in range(len(a) - 2):
    if (a[x] % 113 + a[x + 1] % 113 + a[x + 2] % 113) == k:
        t += 1
        r.append(a[x] + a[x + 1] + a[x + 2])
print(t, max(r))


