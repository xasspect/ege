s = open('173.txt').readlines()
a = []

for i in s:
    a.append(int(i))

k = 0
sm = []

u = []
for i in a:
    if str(i)[-1] == '3' and len(str(abs(i))) == 3:
        u.append(i)


for i in range(len(a) - 2):
    x1 = str(a[i])[-1]
    x2 = str(a[i + 1])[-1]
    x3 = str(a[i + 2])[-1]

    if (int(x1) == 3 and len(str(abs(a[i]))) == 3) or \
            (int(x2) == 3 and len(str(abs(a[i + 1]))) == 3) or \
            (int(x3) == 3 and len(str(abs(a[i + 2]))) == 3):
        if a[i] + a[i + 1] + a[i + 2] < max(u):
            k += 1
            sm.append(a[i] + a[i + 1] + a[i + 2])
print(k, max(sm))

