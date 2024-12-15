from itertools import *
a = product(sorted('МИЗАНТРОП'), repeat=5)
k = 0
for x in a:
    k += 1
    x = ''.join(x)

    if k % 2 == 0:
        if x[0] == 'Н':
            if x.count('Р') == 2:
                print(k, x)