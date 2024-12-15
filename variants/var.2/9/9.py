
from itertools import *
u = []
k = []
o = []
t = permutations('012345', r=6)
for i in t:
    i = ''.join(i)
    y = []
    for j in i:
        y.append(int(j))
    k.append(y)
s = 0
for i in range(len(k)):
    if i % 2 != 0:
        o.append(k[i])



for list in open('9.txt').readlines():
    a = [int(x) for x in list.split()]


    for j in o:
        x1 = [x for x in (j[:2])]
        x2 = [x for x in (j[2:4])]
        x3 = [x for x in (j[4:6])]
        print(x1, x2, x3)
        if (a[x1[0]] + a[x1[1]]) % 2 == 0:

            if (a[x2[0]] + a[x2[1]]) % 2 == 0:
                if (a[x3[0]] + a[x3[1]]) % 2 == 0:
                    s += 1


print(s / 2)



