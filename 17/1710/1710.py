a = list(map(int, open('1710.txt')))
k = int(max([str(x) for x in a if len(str(abs(x))) == 5 and str(x)[-1] == '3']))
s = 0
r = []
for x in range(len(a) - 2):
    if str(a[x])[-1] == '3' or str(a[x + 1])[-1] == '3' or str(a[x + 2])[-1] == '3':
        if a[x] + a[x + 1] + a[x + 2] <= k:
            s += 1
            r.append(a[x] + a[x + 1] + a[x + 2])

print(s, max(r))


