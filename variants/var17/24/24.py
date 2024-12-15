from itertools import permutations
c = permutations('XYZ', r=3)
e = []
for i in c:
    i = ''.join(i)
    e.append(i)
print(e)

a = list(open('24.txt'))[0]
y = []
t = 0
for i in range(0, len(a) - 2, 3):
    x1 = a[i]
    x2 = a[i + 1]
    x3 = a[i + 2]
    if x1 + x2 + x3 in e:
        t += 3
    else:
        y.append(t)
        t = 0
print(max(y))




