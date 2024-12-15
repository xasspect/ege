a = [int(x) for x in open('26.txt')]
a.sort()
a = a[::-1]
v = 835000
m = 0
k = 0
r = []
for i in a:
    if i >= 7000 and i <= 12000:
        if m + i < v:
            k += 1
            m += i
            r.append(i)

print(k, min(r))
