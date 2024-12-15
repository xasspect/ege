s = open('172.txt').readlines()
a = []
for i in s:
    a.append(int(i))

k = 0
sm = []
for i in range(len(a) - 1):
    if a[i] % 16 == min(a) or a[i + 1] % 16 == min(a):
        k += 1
        sm.append(a[i] + a[i + 1])

print(k, max(sm))
