a = list(map(int, open('17.txt')))
m = max(s for s in a if s % 3 == 0)

k = 0
t = []
for x in range(len(a) - 1):
    x1 = a[x]
    x2 = a[x + 1]
    if (x1 % 3 == 0 and x1 != m) or (x2 % 3 == 0 and x2 != m):
        k += 1
        t.append(x1 + x2)

print(k, max(t))

