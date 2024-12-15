from itertools import *
a = product(sorted('abcx'), repeat=5)
k = 0
for i in a:
    i = ''.join(i)

    if 'x' not in i or i[-1] == 'x' and i.count('x') == 1:
        k += 1
print(k)