a = open('24.txt').readlines()
a = [x for x in a[0]]
o = ['Q', 'R', 'S']
r = []
t = []

for i in range(len(a) - 1):
    x1 = a[i]
    x2 = a[i + 1]
    if x1 in o and x2 in o:
        r.append(i)
for x in range(len(r) - 1):
    x1 = r[x]
    x2 = r[x + 1]
    t.append(x2 - x1)
print(max(t))
