a = list(map(int, open('17.txt')))
m = max([s for s in a if s % 3 == 0])
print(m)
k = 0
r = []
for i in range(len(a) - 2):
    x1 = a[i]
    x2 = a[i + 1]
    if x1 % 3 == 0 and x1 != m or x2 % 3 == 0 and x2 != m:
        k += 1
        r.append(x1 + x2)
print(k, max(r))
