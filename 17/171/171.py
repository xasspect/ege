a = open('171.txt').readlines()
s = []
for i in a:
    s.append(int(i))

k = 0
sm = []
for i in range(len(s) - 1):
    x1 = str(s[i])[-1]
    x2 = str(s[i + 1])[-1]

    if int(x1) + int(x2) == 4:
        k += 1
        sm.append(s[i] + s[i + 1])
print(k, min(sm))


