a = list(map(int, open('17.txt')))
t = []
k = 0
for x in range(len(a) - 1):
    x1 = a[x]
    x2 = a[x + 1]
    if str(x1)[0] == '-' or str(x2)[0] == '-':
        if x1 + x2 >= 100:
            k += 1
            t.append(x1 * x2)
print(k, max(t))
print(t)