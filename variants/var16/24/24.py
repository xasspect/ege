a = list(open('24.txt'))[0]
t = '0123456789'
r = []
b = []
for i in range(len(a) - 1):
    x1 = a[i]
    x2 = a[i + 1]
    if x1 in t and int(x1) % 2 != 0 and x2 in t and int(x2) % 2 != 0:
        r.append(i + 1)
for j in range(len(r) - 1):
    c1 = r[j]
    c2 = r[j + 1]
    b.append(c2 - c1)
print(max(b))

