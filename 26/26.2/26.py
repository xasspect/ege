a = [int(x) for x in open('26.txt')]
print(a)
t = []
r = []
j = []

for i in a:
    t.append(i)
    if len(t) == 9:
        y = sorted(t)
        t = sorted(t)[::-1]
        t = t[:-1]
        y = y[:-1]
        j.append(sum(y))
        r.append(sum(t))
        t = []

print(sum(j), sum(r))
