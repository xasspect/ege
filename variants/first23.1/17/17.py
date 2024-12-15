a = [int(x) for x in open('17.txt').readlines()]
k = 0
t = []
b = 0
for q in a:
    if str(q)[-2:] == '13':
        t.append(q)

for i in range(len(a) - 2):

    x1 = a[i]
    x2 = a[i + 1]
    x3 = a[i + 2]

    if (x1 % 2 == 0 and x2 % 2 == 0 and x3 % 2 == 0) or (x1 > 9 or x2 > 9 or x3 > 9):

        if (x1 + x2 + x3) < max(t):
            k += 1
            b += (x1 + x2 + x3)
print(k, b/5887)


