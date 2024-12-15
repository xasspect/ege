a = list(map(int, open('17.txt')))
t = max(a) + min(a)
r = []
k = 0
for i in range(len(a) - 1):
    x1 = a[i]
    x2 = a[i + 1]
    if (x1 + x2) % 2 == 0:
        if x1 + x2 > t:
            k += 1
            r.append(x1 + x2)
print(k, min(r))
