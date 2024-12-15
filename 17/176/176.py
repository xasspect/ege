a = open('176.txt').readlines()
s = [int(x) for x in a]
k = []
t = 117
o = []
for i in range(len(s) - 1):
    if s[i] < 0 and s[i + 1] > 0 or s[i] > 0 and s[i + 1] < 0:
        k += [[s[i], s[i + 1]]]
k.sort()
r = 0
for j in k:
    if j[0] + j[1] % t == 0:
        r += 1
        o.append(j[0] ** 2 + j[1] ** 2)

print(r, min(o))



