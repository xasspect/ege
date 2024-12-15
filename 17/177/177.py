a = open('177.txt')
s = [int(x) for x in a]
t = []
for i in s:
    if str(i)[-2:] == '50':
        t.append(i)
p = 0
q = []
for x in range(len(s) - 2):
    u = []
    if len(str(abs(s[x]))) == 5:

        if s[x] != s[x + 1] and s[x] != s[x + 2]:
            if s[x + 1] != s[x + 2]:
                # print(s[x], s[x + 1], s[x + 2])
                u += s[x], s[x + 1], s[x + 2]
                if sum(u) <= max(t):
                    p += 1
                    q.append(sum(u))
print(p, max(q))


