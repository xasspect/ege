a = list(map(int, open('17.txt')))

k = 0
t = []
for x in range(len(a) - 1):

    if abs(a[x]) % 11 == 0 and abs(a[x + 1]) % 11 == 0:
        k += 1
        t.append(a[x] + a[x + 1])
print(k, max(t))