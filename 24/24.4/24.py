s = open('24.txt').readline()
a = b = l = m = 0
u = []
o = []
for r in range(len(s)):
    a += s[r] == 'X'
    b += s[r] == 'Y'
    while a > 2:
        a -= s[l] == 'X'
        l += 1
    if a == 2:
        u.append([r - l + 1, s[l:r].count('Y')])


p = 0
j = 0
for i in u:
    if p < i[1]:
        p = i[1]
        j = i[0]

print(p, j)

