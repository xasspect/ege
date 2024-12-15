a = list(map(int, open('17.txt')))
k = []
t = 0
for x in range(len(a) - 1):
    x1 = a[x]
    x2 = a[x + 1]
    if x1 % 2 == 0 and x2 % 2 == 0:
        for i in range(101, 200):
            if x1 % i == 0 and x2 % i == 0:
                t += 1
                k.append(x1 - x2)
print(t, max(k))

