s = open('175.txt').readlines()
a = []

for i in s:
    a.append(int(i))

k = 0
sm = []
for i in range(len(a) - 1):
    if a[i] % 55 == min(a) or a[i + 1] % 55 == min(a):
        k += 1
        sm.append(a[i] + a[i + 1])
print(k, min(sm))