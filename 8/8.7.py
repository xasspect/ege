from itertools import *

a = list(product(sorted('012345678'), repeat=7))
k = 0
for x in a:
    if a[0] != '2' and a[0] != '4' and a[0] != '6':
        if a[-1] != a[-2] and a[-1] != a[-3]:
            k += 1
print(k)




