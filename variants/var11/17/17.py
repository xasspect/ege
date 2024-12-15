
a = list(map(int, open('17.txt')))

p = len([s for s in a if len(str(s)) == 2])
t = []
k = 0
for x in range(len(a) - 1):
    x1 = a[x]
    x2 = a[x + 1]
    if int(str(x1)[-1]) + int(str(x2)[-1]) == p:
        k += 1
        t.append(x1 + x2)
print(k, max(t))

