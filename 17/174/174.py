s = open('174.txt').readlines()
a = []
for i in s:
    a.append(int(i))

u = []
for i in a:
    if i % 32 == 0:
        u.append(i)


k = 0
sm = []
for i in range(len(a) - 1):
    if str(a[i])[0] == '-' or str(a[i + 1])[0] == '-':
        if (a[i] + a[i + 1]) < len(u):
            k += 1
            sm.append(a[i] + a[i + 1])
print(k, max(sm))
