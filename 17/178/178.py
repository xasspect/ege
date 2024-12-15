a = open('178.txt').readlines()
s = [int(x) for x in a]
print(s)
k = []
for j in s:
    if str(j)[-2:] == '18':
        k.append(j)


r = 0
q = []
for i in range(len(s) - 2):
    if len(str(s[i])) == 5 or len(str(s[i + 1])) == 5 or len(str(s[i + 2])) == 5:
        if (s[i] * s[i + 1] * s[i + 2]) % max(k) == 0:

            q.append(s[i] * s[i + 1] * s[i + 2])
            r += 1
print(r, max(q))

